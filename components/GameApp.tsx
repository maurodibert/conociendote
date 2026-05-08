"use client";

import { AnimatePresence } from "framer-motion";
import { useGame } from "@/lib/GameContext";
import WelcomeScreen from "./screens/WelcomeScreen";
import CategoryReveal from "./screens/CategoryReveal";
import LevelSelect from "./screens/LevelSelect";
import QuestionScreen from "./screens/QuestionScreen";
import PeerRatingScreen from "./screens/PeerRatingScreen";
import ResultScreen from "./screens/ResultScreen";
import ScoreboardScreen from "./screens/ScoreboardScreen";

export default function GameApp() {
  const { state } = useGame();

  return (
    <div className="h-full overflow-hidden relative">
      {/* Ambient background shapes */}
      <div className="fixed inset-0 pointer-events-none overflow-hidden">
        <div className="absolute -top-32 -right-32 w-80 h-80 rounded-full bg-[#6BB5B5]/6 blur-[80px]" />
        <div className="absolute bottom-0 -left-20 w-64 h-64 rounded-full bg-[#B5A8CE]/6 blur-[60px]" />
        <div className="absolute top-1/2 -right-10 w-48 h-48 rounded-full bg-[#E8B86A]/5 blur-[50px]" />
      </div>

      <div className="relative h-full overflow-y-auto">
        <AnimatePresence mode="wait">
          {state.screen === "welcome" && <WelcomeScreen key="welcome" />}
          {state.screen === "reveal" && <CategoryReveal key="reveal" />}
          {state.screen === "level-select" && <LevelSelect key="level-select" />}
          {state.screen === "question" && <QuestionScreen key="question" />}
          {state.screen === "peer-rating" && <PeerRatingScreen key="peer-rating" />}
          {state.screen === "result" && <ResultScreen key="result" />}
          {state.screen === "scoreboard" && <ScoreboardScreen key="scoreboard" />}
        </AnimatePresence>
      </div>
    </div>
  );
}
