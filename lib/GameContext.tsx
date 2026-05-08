"use client";

import React, { createContext, useCallback, useContext, useMemo, useReducer, useRef } from "react";
import { Category, GameState, Level, Player } from "./types";
import {
  applyApproved, applyPassed, createPlayer, getAvailableCategoryIds,
  getStreakPrivileges, nextTurn, pickQuestion, pickRandomCategory, submitRating,
} from "./gameLogic";

type Action =
  | { type: "START"; players: string[]; spiceEnabled: boolean }
  | { type: "SELECT_CATEGORY"; category: Category }
  | { type: "SELECT_LEVEL"; level: Level }
  | { type: "SHOW_QUESTION" }
  | { type: "APPROVED" }
  | { type: "PASSED" }
  | { type: "SUBMIT_RATING"; rating: number }
  | { type: "NEXT_TURN" }
  | { type: "SHOW_SCOREBOARD" }
  | { type: "RESTART" };

const initialState: GameState = {
  players: [],
  currentPlayerIndex: 0,
  screen: "welcome",
  selectedCategory: null,
  selectedLevel: null,
  currentQuestion: null,
  round: 1,
  spiceEnabled: false,
  lastOutcome: null,
  canChooseCategory: false,
  maxLevel: 1,
  pendingRatings: [],
  ratingVoterIndex: 0,
  ratingPointsEarned: 0,
};

function reducer(state: GameState, action: Action): GameState {
  switch (action.type) {
    case "START":
      return {
        ...initialState,
        players: action.players.map((name, i) => createPlayer(name, i)),
        spiceEnabled: action.spiceEnabled,
        screen: "reveal",
      };

    case "SELECT_CATEGORY":
      return { ...state, selectedCategory: action.category, screen: "level-select" };

    case "SELECT_LEVEL":
      return { ...state, selectedLevel: action.level };

    case "SHOW_QUESTION":
      return { ...state, screen: "question" };

    case "APPROVED":
      return applyApproved(state);

    case "PASSED":
      return applyPassed(state);

    case "SUBMIT_RATING":
      return submitRating(state, action.rating);

    case "NEXT_TURN":
      return nextTurn(state, state.players.length);

    case "SHOW_SCOREBOARD":
      return { ...state, screen: "scoreboard" };

    case "RESTART":
      return { ...initialState };

    default:
      return state;
  }
}

interface GameContextValue {
  state: GameState;
  categories: Category[];
  allCategories: Category[];
  dispatch: React.Dispatch<Action>;
  getRandomCategory: () => Category;
  getQuestion: (category: Category, level: Level) => ReturnType<typeof pickQuestion>;
}

const GameContext = createContext<GameContextValue | null>(null);

export function GameProvider({ children, categories }: { children: React.ReactNode; categories: Category[] }) {
  const [state, dispatch] = useReducer(reducer, initialState);
  const usedIds = useRef(new Set<string>());

  // All categories gated by spiceEnabled (age gate)
  const spiceGatedCategories = useMemo(
    () => state.spiceEnabled ? categories : categories.filter((c) => !["sinFiltro", "confesiones", "fantasias"].includes(c.id)),
    [categories, state.spiceEnabled]
  );

  // Categories available for random pick (current player's unlocked set)
  const currentPlayerPoints = state.players[state.currentPlayerIndex]?.points ?? 0;
  const availableIds = useMemo(
    () => getAvailableCategoryIds(currentPlayerPoints),
    [currentPlayerPoints]
  );

  const categories_available = useMemo(
    () => spiceGatedCategories.filter((c) => availableIds.has(c.id)),
    [spiceGatedCategories, availableIds]
  );

  const getRandomCategory = useCallback(
    () => pickRandomCategory(categories_available, state.selectedCategory?.id),
    [categories_available, state.selectedCategory?.id]
  );

  const getQuestion = useCallback(
    (category: Category, level: Level) => {
      const q = pickQuestion(category, level, usedIds.current);
      if (q) usedIds.current.add(q.id);
      return q;
    },
    []
  );

  const value = useMemo(
    () => ({
      state,
      categories: categories_available,
      allCategories: spiceGatedCategories,
      dispatch,
      getRandomCategory,
      getQuestion,
    }),
    [state, categories_available, spiceGatedCategories, dispatch, getRandomCategory, getQuestion]
  );

  return <GameContext.Provider value={value}>{children}</GameContext.Provider>;
}

export function useGame() {
  const ctx = useContext(GameContext);
  if (!ctx) throw new Error("useGame must be inside GameProvider");
  return ctx;
}
