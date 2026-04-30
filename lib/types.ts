export interface Question {
  id: string;
  text: string;
  level: 1 | 2 | 3;
}

export interface Category {
  id: string;
  name: string;
  shortName: string;
  color: string;
  shadowColor: string;
  questions: Question[];
}

export interface Player {
  id: string;
  name: string;
  points: number;
  streak: number;    // consecutive approved truths
  passes: number;
  answers: number;
}

export type Level = 1 | 2 | 3;

export type GameScreen =
  | "welcome"
  | "reveal"
  | "level-select"
  | "question"
  | "result"
  | "scoreboard";

export interface GameState {
  players: Player[];
  currentPlayerIndex: number;
  screen: GameScreen;
  selectedCategory: Category | null;
  selectedLevel: Level | null;
  currentQuestion: Question | null;
  round: number;
  spiceEnabled: boolean;
  lastOutcome: "approved" | "passed" | null;
  canChooseCategory: boolean;
  maxLevel: Level;
}
