"use client";

import { motion } from "framer-motion";
import { useGame } from "@/lib/GameContext";

export default function ScoreboardScreen() {
  const { state, dispatch } = useGame();
  const sorted = [...state.players].sort((a, b) => b.points - a.points);
  const maxPoints = sorted[0]?.points || 1;

  const medals = ["#E8B86A", "#8AAAB8", "#CC9A4A"];

  return (
    <motion.div
      className="flex flex-col min-h-full px-5 py-12"
      initial={{ opacity: 0, y: 24 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -16 }}
      transition={{ duration: 0.35 }}
    >
      <h2 className="text-2xl font-bold text-[#1A2535] tracking-tight mb-8 text-center">Puntajes</h2>

      <div className="space-y-3 mb-10">
        {sorted.map((player, i) => {
          const width = maxPoints > 0 ? (player.points / maxPoints) * 100 : 0;
          return (
            <motion.div
              key={player.id}
              initial={{ opacity: 0, x: -16 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: i * 0.08 }}
              className="bg-[#E8E0D0] border border-[#D0C6B2] rounded-2xl p-4"
            >
              <div className="flex items-center justify-between mb-3">
                <div className="flex items-center gap-3">
                  {i < 3 && (
                    <div
                      className="w-7 h-7 rounded-full flex items-center justify-center text-xs font-bold text-white"
                      style={{ backgroundColor: medals[i] }}
                    >
                      {i + 1}
                    </div>
                  )}
                  {i >= 3 && (
                    <div className="w-7 h-7 rounded-full flex items-center justify-center text-xs text-[#1A2535]/40 bg-[#DDD4C2]">
                      {i + 1}
                    </div>
                  )}
                  <span className="font-semibold text-sm text-[#1A2535]">{player.name}</span>
                </div>
                <span className="text-xl font-bold text-[#6BB5B5]">{player.points}</span>
              </div>
              <div className="h-1.5 bg-[#D0C6B2] rounded-full overflow-hidden">
                <motion.div
                  className="h-full rounded-full"
                  style={{ backgroundColor: i === 0 ? "#E8B86A" : "#6BB5B5" }}
                  initial={{ width: 0 }}
                  animate={{ width: `${width}%` }}
                  transition={{ duration: 0.6, delay: i * 0.08 + 0.2, ease: "easeOut" }}
                />
              </div>
              <div className="flex justify-between mt-2">
                <span className="text-xs text-[#1A2535]/35">
                  {player.answers} resp · {player.passes} paso{player.passes !== 1 ? "s" : ""}
                </span>
                {player.streak > 0 && (
                  <span className="text-xs font-medium" style={{ color: "#CC9A4A" }}>
                    Racha {player.streak}
                  </span>
                )}
              </div>
            </motion.div>
          );
        })}
      </div>

      <div className="mt-auto space-y-3">
        <motion.button
          onClick={() => dispatch({ type: "NEXT_TURN" })}
          whileTap={{ scale: 0.97 }}
          className="w-full py-4 rounded-xl font-semibold text-sm bg-[#6BB5B5] hover:bg-[#4A9494] text-white shadow-lg shadow-[#6BB5B5]/25 transition-colors"
        >
          Continuar jugando
        </motion.button>
        <button
          onClick={() => dispatch({ type: "RESTART" })}
          className="w-full py-3 rounded-xl text-sm text-[#1A2535]/40 hover:text-[#D4888A] transition-colors"
        >
          Nueva partida
        </button>
      </div>
    </motion.div>
  );
}
