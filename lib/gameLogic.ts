import { Category, GameState, Level, Player, Question } from "./types";

export const POINTS_BY_LEVEL: Record<Level, number> = { 1: 10, 2: 20, 3: 40 };

export function createPlayer(name: string, index: number): Player {
  return { id: `p${index}`, name, points: 0, streak: 0, passes: 0, answers: 0 };
}

export function getStreakPrivileges(streak: number): { canChooseCategory: boolean; maxLevel: Level } {
  if (streak >= 5) return { canChooseCategory: true, maxLevel: 3 };
  if (streak >= 3) return { canChooseCategory: true, maxLevel: 2 };
  return { canChooseCategory: false, maxLevel: 1 };
}

export function pickRandomCategory(categories: Category[], excludeId?: string): Category {
  const pool = excludeId ? categories.filter((c) => c.id !== excludeId) : categories;
  return pool[Math.floor(Math.random() * pool.length)];
}

export function pickQuestion(category: Category, level: Level, usedIds: Set<string>): Question | null {
  const pool = category.questions.filter((q) => q.level === level && !usedIds.has(q.id));
  if (!pool.length) {
    // fallback: ignore used
    const fallback = category.questions.filter((q) => q.level === level);
    return fallback[Math.floor(Math.random() * fallback.length)] ?? null;
  }
  return pool[Math.floor(Math.random() * pool.length)];
}

export function applyApproved(state: GameState): GameState {
  const players = [...state.players];
  const player = { ...players[state.currentPlayerIndex] };
  const pts = POINTS_BY_LEVEL[state.selectedLevel!];
  player.points += pts;
  player.streak += 1;
  player.answers += 1;
  players[state.currentPlayerIndex] = player;
  const { canChooseCategory, maxLevel } = getStreakPrivileges(player.streak);
  return { ...state, players, screen: "result", lastOutcome: "approved", canChooseCategory, maxLevel };
}

export function applyPassed(state: GameState): GameState {
  const players = [...state.players];
  const player = { ...players[state.currentPlayerIndex] };
  player.streak = 0;
  player.passes += 1;
  players[state.currentPlayerIndex] = player;
  return { ...state, players, screen: "result", lastOutcome: "passed", canChooseCategory: false, maxLevel: 1 };
}

export function nextTurn(state: GameState, playersCount: number): GameState {
  const next = (state.currentPlayerIndex + 1) % playersCount;
  const { canChooseCategory, maxLevel } = getStreakPrivileges(state.players[next].streak);
  return {
    ...state,
    currentPlayerIndex: next,
    screen: "reveal",
    selectedCategory: null,
    selectedLevel: null,
    currentQuestion: null,
    round: state.round + 1,
    lastOutcome: null,
    canChooseCategory,
    maxLevel,
  };
}
