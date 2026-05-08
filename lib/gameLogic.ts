import { Category, GameState, Level, Player, Question } from "./types";

export const CATEGORY_UNLOCK_POINTS: Record<string, number> = {
  sinFiltro: 15,
  confesiones: 35,
  fantasias: 60,
};

// Base categories always available
const BASE_CATEGORY_IDS = new Set([
  "infancia", "futuro", "amor", "familia", "amistades",
  "exs", "personalidad", "miedos", "logros",
]);

export function getAvailableCategoryIds(playerPoints: number): Set<string> {
  const ids = new Set(BASE_CATEGORY_IDS);
  for (const [catId, threshold] of Object.entries(CATEGORY_UNLOCK_POINTS)) {
    if (playerPoints >= threshold) ids.add(catId);
  }
  return ids;
}

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
    const fallback = category.questions.filter((q) => q.level === level);
    return fallback[Math.floor(Math.random() * fallback.length)] ?? null;
  }
  return pool[Math.floor(Math.random() * pool.length)];
}

export function applyApproved(state: GameState): GameState {
  return {
    ...state,
    screen: "peer-rating",
    lastOutcome: "approved",
    pendingRatings: [],
    ratingVoterIndex: 0,
    ratingPointsEarned: 0,
  };
}

export function submitRating(state: GameState, rating: number): GameState {
  const otherPlayers = state.players
    .map((p, i) => ({ p, i }))
    .filter(({ i }) => i !== state.currentPlayerIndex);

  const newRatings = [...state.pendingRatings, rating];
  const nextVoterIndex = state.ratingVoterIndex + 1;

  if (nextVoterIndex >= otherPlayers.length) {
    // All voted — finalize
    const avg = Math.round(newRatings.reduce((a, b) => a + b, 0) / newRatings.length);
    const players = [...state.players];
    const player = { ...players[state.currentPlayerIndex] };
    player.points += avg;
    player.streak += 1;
    player.answers += 1;
    players[state.currentPlayerIndex] = player;
    const { canChooseCategory, maxLevel } = getStreakPrivileges(player.streak);
    return {
      ...state,
      players,
      screen: "result",
      pendingRatings: newRatings,
      ratingPointsEarned: avg,
      canChooseCategory,
      maxLevel,
    };
  }

  return {
    ...state,
    pendingRatings: newRatings,
    ratingVoterIndex: nextVoterIndex,
  };
}

export function applyPassed(state: GameState): GameState {
  const players = [...state.players];
  const player = { ...players[state.currentPlayerIndex] };
  player.streak = 0;
  player.passes += 1;
  players[state.currentPlayerIndex] = player;
  return { ...state, players, screen: "result", lastOutcome: "passed", ratingPointsEarned: 0, canChooseCategory: false, maxLevel: 1 };
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
    pendingRatings: [],
    ratingVoterIndex: 0,
    ratingPointsEarned: 0,
  };
}
