"use client";

import { motion } from "framer-motion";
import { useEffect, useState } from "react";
import { useGame } from "@/lib/GameContext";
import { Question } from "@/lib/types";

const LEVEL_LABELS: Record<number, { name: string; color: string; bgColor: string; borderColor: string }> = {
  1: { name: "Suave", color: "#4A9494", bgColor: "#6BB5B515", borderColor: "#6BB5B530" },
  2: { name: "Medio", color: "#CC9A4A", bgColor: "#E8B86A15", borderColor: "#E8B86A30" },
  3: { name: "Profundo", color: "#B56870", bgColor: "#D4888A15", borderColor: "#D4888A30" },
};

export default function QuestionScreen() {
  const { state, dispatch, getQuestion } = useGame();
  const cat = state.selectedCategory!;
  const level = state.selectedLevel!;
  const currentPlayer = state.players[state.currentPlayerIndex];
  const [question, setQuestion] = useState<Question | null>(null);
  const lbl = LEVEL_LABELS[level];

  useEffect(() => {
    const q = getQuestion(cat, level);
    setQuestion(q);
  }, [cat, level, getQuestion]);

  if (!question) {
    return (
      <div className="flex items-center justify-center min-h-full">
        <div className="w-8 h-8 rounded-full border-2 border-[#D0C6B2] border-t-[#6BB5B5] animate-spin" />
      </div>
    );
  }

  return (
    <motion.div
      className="flex flex-col items-center justify-between min-h-full px-5 py-12"
      initial={{ opacity: 0, y: 24 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -16 }}
      transition={{ duration: 0.35, ease: "easeOut" }}
    >
      {/* Top: category + level */}
      <div className="flex items-center gap-2 self-start">
        <span className="text-sm font-medium" style={{ color: cat.color }}>
          {cat.shortName}
        </span>
        <span className="text-[#D0C6B2]">·</span>
        <span
          className="text-xs font-medium px-2.5 py-0.5 rounded-full border"
          style={{ color: lbl.color, backgroundColor: lbl.bgColor, borderColor: lbl.borderColor }}
        >
          {lbl.name}
        </span>
      </div>

      {/* Question */}
      <motion.div
        className="flex-1 flex items-center justify-center py-10"
        initial={{ opacity: 0, scale: 0.95 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ delay: 0.15, duration: 0.4 }}
      >
        <div className="text-center">
          <div
            className="inline-block px-3 py-1 rounded-full text-xs font-medium mb-6"
            style={{ backgroundColor: `${cat.color}15`, color: cat.color }}
          >
            para {currentPlayer.name}
          </div>
          <p className="text-2xl font-light text-[#1A2535] leading-relaxed tracking-tight">
            {question.text}
          </p>
        </div>
      </motion.div>

      {/* Action buttons */}
      <motion.div
        className="w-full space-y-3"
        initial={{ opacity: 0, y: 12 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3 }}
      >
        <p className="text-center text-xs text-[#1A2535]/35 font-light mb-4">
          Respondé la pregunta — el grupo decide si fue verdad
        </p>
        <motion.button
          onClick={() => dispatch({ type: "APPROVED" })}
          whileTap={{ scale: 0.97 }}
          className="w-full py-4 rounded-xl font-semibold text-sm text-white shadow-lg transition-colors"
          style={{
            backgroundColor: "#8FB5A4",
            boxShadow: "0 8px 24px #8FB5A440",
          }}
        >
          El grupo aprueba — fue verdad
        </motion.button>
        <motion.button
          onClick={() => dispatch({ type: "PASSED" })}
          whileTap={{ scale: 0.97 }}
          className="w-full py-3.5 rounded-xl font-medium text-sm bg-[#E8E0D0] border border-[#D0C6B2] text-[#1A2535]/50 hover:bg-[#DDD4C2] transition-all"
        >
          Paso — prefiero no responder
        </motion.button>
      </motion.div>
    </motion.div>
  );
}
