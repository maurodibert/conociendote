"use client";

import { motion } from "framer-motion";
import { useState } from "react";
import { useGame } from "@/lib/GameContext";

export default function PeerRatingScreen() {
  const { state, dispatch } = useGame();
  const [selected, setSelected] = useState<number | null>(null);
  const [confirmed, setConfirmed] = useState(false);

  const answerer = state.players[state.currentPlayerIndex];
  const otherPlayers = state.players
    .map((p, i) => ({ p, i }))
    .filter(({ i }) => i !== state.currentPlayerIndex);

  const currentVoter = otherPlayers[state.ratingVoterIndex];
  const votesLeft = otherPlayers.length - state.ratingVoterIndex;
  const isLast = state.ratingVoterIndex === otherPlayers.length - 1;

  function handleConfirm() {
    if (selected === null || confirmed) return;
    setConfirmed(true);
    setTimeout(() => {
      dispatch({ type: "SUBMIT_RATING", rating: selected });
      setSelected(null);
      setConfirmed(false);
    }, 400);
  }

  const ratingColor = (n: number) => {
    if (n <= 3) return "#D4888A";
    if (n <= 6) return "#E8B86A";
    if (n <= 8) return "#6BB5B5";
    return "#9B84CC";
  };

  return (
    <motion.div
      className="flex flex-col items-center justify-between min-h-full px-5 py-10"
      initial={{ opacity: 0, x: 24 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: -24 }}
      transition={{ duration: 0.3 }}
    >
      {/* Top */}
      <div className="w-full text-center space-y-1">
        <p className="text-xs text-[#1A2535]/35 font-light uppercase tracking-widest">Votando respuesta de</p>
        <p className="text-xl font-bold text-[#1A2535]">{answerer.name}</p>
      </div>

      {/* Question recap */}
      <div className="w-full max-w-sm bg-[#E8E0D0] border border-[#D0C6B2] rounded-2xl px-5 py-4">
        <p className="text-xs text-[#1A2535]/40 mb-2 font-light">Pregunta</p>
        <p className="text-sm text-[#1A2535]/75 leading-relaxed italic">
          &ldquo;{state.currentQuestion?.text}&rdquo;
        </p>
      </div>

      {/* Voter turn */}
      <div className="w-full max-w-sm text-center space-y-1">
        <motion.p
          key={currentVoter.p.id}
          initial={{ opacity: 0, y: 6 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-base font-semibold text-[#1A2535]"
        >
          {currentVoter.p.name}, tu voto
        </motion.p>
        <p className="text-xs text-[#1A2535]/35">
          {state.ratingVoterIndex + 1} de {otherPlayers.length}
        </p>
      </div>

      {/* Rating grid 1-10 */}
      <div className="w-full max-w-sm">
        <div className="grid grid-cols-5 gap-2.5">
          {Array.from({ length: 10 }, (_, i) => i + 1).map((n) => {
            const isSelected = selected === n;
            const color = ratingColor(n);
            return (
              <motion.button
                key={n}
                onClick={() => !confirmed && setSelected(n)}
                whileTap={{ scale: 0.92 }}
                className="aspect-square rounded-xl flex items-center justify-center text-base font-bold transition-all duration-150"
                style={{
                  backgroundColor: isSelected ? color : `${color}18`,
                  color: isSelected ? "white" : color,
                  boxShadow: isSelected ? `0 4px 16px ${color}50` : undefined,
                  border: `1.5px solid ${isSelected ? color : `${color}40`}`,
                }}
                animate={{ scale: isSelected ? 1.08 : 1 }}
                transition={{ type: "spring", stiffness: 300, damping: 20 }}
              >
                {n}
              </motion.button>
            );
          })}
        </div>

        {/* Confirm button */}
        <motion.button
          onClick={handleConfirm}
          disabled={selected === null || confirmed}
          whileTap={{ scale: 0.97 }}
          className="w-full mt-5 py-4 rounded-xl font-semibold text-sm transition-all duration-200"
          animate={{
            backgroundColor: selected !== null ? ratingColor(selected) : "#D0C6B2",
            opacity: selected !== null ? 1 : 0.5,
          }}
          style={{ color: "white" }}
        >
          {confirmed ? "Votado ✓" : isLast ? "Votar y ver resultado" : "Votar"}
        </motion.button>
      </div>

      {/* Progress dots */}
      <div className="flex gap-2">
        {otherPlayers.map((_, i) => (
          <div
            key={i}
            className="w-2 h-2 rounded-full transition-all duration-300"
            style={{
              backgroundColor: i < state.ratingVoterIndex
                ? "#6BB5B5"
                : i === state.ratingVoterIndex
                ? "#1A2535"
                : "#D0C6B2",
            }}
          />
        ))}
      </div>
    </motion.div>
  );
}
