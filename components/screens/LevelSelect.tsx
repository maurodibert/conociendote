"use client";

import { motion } from "framer-motion";
import { useGame } from "@/lib/GameContext";
import { Level } from "@/lib/types";
import { CATEGORY_ICONS } from "@/components/icons/IsometricIcons";

const LEVELS: { level: Level; name: string; desc: string; color: string; bgColor: string; borderColor: string }[] = [
  {
    level: 1,
    name: "Suave",
    desc: "Cómoda, liviana, para romper el hielo",
    color: "#4A9494",
    bgColor: "#6BB5B515",
    borderColor: "#6BB5B530",
  },
  {
    level: 2,
    name: "Medio",
    desc: "Personal, requiere un poco de confianza",
    color: "#CC9A4A",
    bgColor: "#E8B86A15",
    borderColor: "#E8B86A30",
  },
  {
    level: 3,
    name: "Profundo",
    desc: "Íntima, vulnerable, requiere coraje",
    color: "#B56870",
    bgColor: "#D4888A15",
    borderColor: "#D4888A30",
  },
];

export default function LevelSelect() {
  const { state, dispatch, getQuestion } = useGame();
  const cat = state.selectedCategory!;
  const Icon = CATEGORY_ICONS[cat.id];
  const maxLevel = state.maxLevel;

  function select(level: Level) {
    if (level > maxLevel) return;
    dispatch({ type: "SELECT_LEVEL", level });
    dispatch({ type: "SHOW_QUESTION" });
  }

  return (
    <motion.div
      className="flex flex-col items-center justify-center min-h-full px-5 py-12"
      initial={{ opacity: 0, y: 24 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -16 }}
      transition={{ duration: 0.35, ease: "easeOut" }}
    >
      {/* Category header */}
      <div className="flex flex-col items-center mb-10">
        <div
          className="w-20 h-20 rounded-2xl flex items-center justify-center mb-4"
          style={{ backgroundColor: `${cat.color}15`, border: `1px solid ${cat.color}30` }}
        >
          {Icon && <Icon color={cat.color} shadowColor={cat.shadowColor} size={52} />}
        </div>
        <h2 className="text-2xl font-bold text-[#1A2535] tracking-tight">{cat.name}</h2>
        <p className="text-sm text-[#1A2535]/40 mt-1 font-light">
          {state.players[state.currentPlayerIndex].name}, elegí el nivel
        </p>
      </div>

      {/* Streak indicator */}
      {state.players[state.currentPlayerIndex].streak > 0 && (
        <motion.div
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          className="mb-6 px-4 py-2 rounded-full border"
          style={{ backgroundColor: "#E8B86A10", borderColor: "#E8B86A30" }}
        >
          <p className="text-xs font-medium" style={{ color: "#CC9A4A" }}>
            Racha {state.players[state.currentPlayerIndex].streak} — {maxLevel === 3 ? "acceso completo" : maxLevel === 2 ? "hasta Medio" : "nivel Suave"}
          </p>
        </motion.div>
      )}

      {/* Level options */}
      <div className="w-full max-w-sm space-y-3">
        {LEVELS.map(({ level, name, desc, color, bgColor, borderColor }, i) => {
          const locked = level > maxLevel;
          return (
            <motion.button
              key={level}
              onClick={() => !locked && select(level)}
              initial={{ opacity: 0, x: -12 }}
              animate={{ opacity: locked ? 0.35 : 1, x: 0 }}
              transition={{ delay: i * 0.08, duration: 0.3 }}
              whileTap={locked ? {} : { scale: 0.97 }}
              className={`w-full flex items-center gap-4 p-4 rounded-xl border text-left transition-all duration-200 ${
                locked ? "cursor-not-allowed" : "cursor-pointer hover:scale-[1.01]"
              }`}
              style={{
                backgroundColor: bgColor,
                borderColor: borderColor,
              }}
            >
              <div
                className="w-10 h-10 rounded-lg flex items-center justify-center flex-shrink-0 font-bold text-sm"
                style={{ backgroundColor: `${color}25`, color }}
              >
                {level}
              </div>
              <div className="flex-1">
                <p className="font-semibold text-sm" style={{ color }}>
                  {name}
                </p>
                <p className="text-xs text-[#1A2535]/45 mt-0.5 font-light">{desc}</p>
              </div>
              {locked && (
                <svg width="16" height="16" viewBox="0 0 16 16" fill="none" className="flex-shrink-0">
                  <rect x="3" y="7" width="10" height="8" rx="2" fill="#1A2535" opacity="0.2" />
                  <path d="M5 7V5a3 3 0 016 0v2" stroke="#1A2535" strokeWidth="1.5" opacity="0.2" />
                </svg>
              )}
            </motion.button>
          );
        })}
      </div>

      {maxLevel < 3 && (
        <p className="mt-6 text-xs text-[#1A2535]/30 text-center max-w-xs font-light">
          Respondé preguntas para desbloquear niveles más profundos
        </p>
      )}
    </motion.div>
  );
}
