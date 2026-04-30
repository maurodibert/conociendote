"use client";

import { motion } from "framer-motion";
import { useGame } from "@/lib/GameContext";
import { POINTS_BY_LEVEL } from "@/lib/gameLogic";

export default function ResultScreen() {
  const { state, dispatch } = useGame();
  const playerIndex = state.currentPlayerIndex;
  const player = state.players[playerIndex];
  const level = state.selectedLevel!;
  const passed = state.lastOutcome === "passed";
  const points = passed ? 0 : POINTS_BY_LEVEL[level];
  const nextPlayer = state.players[(playerIndex + 1) % state.players.length];

  return (
    <motion.div
      className="flex flex-col items-center justify-center min-h-full px-5 py-12 gap-8"
      initial={{ opacity: 0, scale: 0.96 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0 }}
      transition={{ duration: 0.3 }}
    >
      {/* Result icon */}
      <motion.div
        initial={{ scale: 0 }}
        animate={{ scale: 1 }}
        transition={{ type: "spring", stiffness: 200, damping: 15, delay: 0.1 }}
      >
        {passed ? (
          <div className="w-20 h-20 rounded-full bg-[#D0C6B2]/40 border border-[#D0C6B2] flex items-center justify-center">
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
              <line x1="8" y1="8" x2="24" y2="24" stroke="#1A2535" strokeWidth="2" strokeLinecap="round" opacity="0.3" />
              <line x1="24" y1="8" x2="8" y2="24" stroke="#1A2535" strokeWidth="2" strokeLinecap="round" opacity="0.3" />
            </svg>
          </div>
        ) : (
          <div
            className="w-20 h-20 rounded-full flex items-center justify-center"
            style={{ backgroundColor: "#8FB5A420", border: "1px solid #8FB5A440" }}
          >
            <svg width="32" height="32" viewBox="0 0 32 32" fill="none">
              <path d="M8 16L13 21L24 10" stroke="#6E9487" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round" />
            </svg>
          </div>
        )}
      </motion.div>

      {/* Message */}
      <div className="text-center space-y-2">
        {passed ? (
          <>
            <p className="text-xl font-semibold text-[#1A2535]">Pasó</p>
            <p className="text-sm text-[#1A2535]/40 font-light">Sin puntos esta ronda · Racha cortada</p>
          </>
        ) : (
          <>
            <p className="text-xl font-semibold text-[#1A2535]">Aprobado</p>
            <motion.p
              className="text-4xl font-bold"
              style={{ color: "#6BB5B5" }}
              initial={{ opacity: 0, y: 8 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: 0.3 }}
            >
              +{points}
            </motion.p>
            <p className="text-sm text-[#1A2535]/40 font-light">Total: {player.points} pts</p>
          </>
        )}
      </div>

      {/* Streak badge */}
      {!passed && player.streak > 0 && (
        <motion.div
          initial={{ opacity: 0, y: 8 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4 }}
          className="px-5 py-3 rounded-xl border text-center"
          style={{ backgroundColor: "#E8B86A10", borderColor: "#E8B86A30" }}
        >
          <p className="text-sm font-semibold" style={{ color: "#CC9A4A" }}>
            Racha {player.streak}
          </p>
          <p className="text-xs text-[#1A2535]/40 mt-0.5 font-light">
            {player.streak >= 5
              ? "Acceso total desbloqueado"
              : player.streak >= 3
              ? "Podés elegir categoría y nivel Medio"
              : `${3 - player.streak} más para elegir categoría y nivel Medio`}
          </p>
        </motion.div>
      )}

      {/* Score summary */}
      <div className="w-full max-w-sm bg-[#E8E0D0] border border-[#D0C6B2] rounded-2xl p-4 space-y-2">
        {state.players.map((p, i) => (
          <div key={p.id} className="flex items-center justify-between">
            <span className={`text-sm ${i === playerIndex ? "font-semibold text-[#1A2535]" : "text-[#1A2535]/50"}`}>
              {p.name}
            </span>
            <span className={`text-sm font-bold ${i === playerIndex ? "text-[#6BB5B5]" : "text-[#1A2535]/30"}`}>
              {p.points}
            </span>
          </div>
        ))}
      </div>

      {/* Actions */}
      <div className="w-full max-w-sm space-y-3">
        <p className="text-center text-xs text-[#1A2535]/35">
          Turno de <span className="font-medium text-[#1A2535]/60">{nextPlayer.name}</span>
        </p>
        <motion.button
          onClick={() => dispatch({ type: "NEXT_TURN" })}
          whileTap={{ scale: 0.97 }}
          className="w-full py-4 rounded-xl font-semibold text-sm bg-[#6BB5B5] hover:bg-[#4A9494] text-white shadow-lg shadow-[#6BB5B5]/25 transition-colors"
        >
          Siguiente turno
        </motion.button>
        <button
          onClick={() => dispatch({ type: "SHOW_SCOREBOARD" })}
          className="w-full py-3 rounded-xl text-sm text-[#1A2535]/40 hover:text-[#1A2535]/60 transition-colors"
        >
          Ver puntajes
        </button>
      </div>
    </motion.div>
  );
}
