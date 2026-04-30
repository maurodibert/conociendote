"use client";

import { AnimatePresence, motion } from "framer-motion";
import { useState } from "react";
import { useGame } from "@/lib/GameContext";

export default function WelcomeScreen() {
  const { dispatch } = useGame();
  const [names, setNames] = useState(["", ""]);
  const [spice, setSpice] = useState(false);
  const [focusIdx, setFocusIdx] = useState<number | null>(null);

  const validPlayers = names.filter((n) => n.trim().length > 0);

  function addPlayer() {
    if (names.length < 8) setNames([...names, ""]);
  }
  function removePlayer(i: number) {
    if (names.length <= 2) return;
    setNames(names.filter((_, idx) => idx !== i));
  }
  function updateName(i: number, val: string) {
    const next = [...names];
    next[i] = val;
    setNames(next);
  }
  function start() {
    if (validPlayers.length < 2) return;
    dispatch({ type: "START", players: validPlayers, spiceEnabled: spice });
  }

  return (
    <motion.div
      className="flex flex-col items-center justify-center min-h-full px-5 py-10"
      initial={{ opacity: 0, y: 24 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -16 }}
      transition={{ duration: 0.4, ease: "easeOut" }}
    >
      {/* Logo / hero */}
      <div className="mb-10 text-center">
        <div className="inline-flex items-center justify-center w-20 h-20 mb-5 relative">
          {/* Isometric logo cube */}
          <svg width="80" height="70" viewBox="0 0 80 70" fill="none">
            <polygon points="40,4 74,22 40,40 6,22" fill="#6BB5B5" opacity="0.95" />
            <polygon points="6,22 40,40 40,66 6,48" fill="#4A9494" opacity="0.7" />
            <polygon points="40,40 74,22 74,48 40,66" fill="#3A7A7A" opacity="0.5" />
          </svg>
        </div>
        <h1 className="text-3xl font-bold text-[#1A2535] tracking-tight">Conociéndote</h1>
        <p className="text-sm text-[#1A2535]/50 mt-1.5 font-light">El juego de las preguntas que importan</p>
      </div>

      {/* Players */}
      <div className="w-full max-w-sm space-y-2.5 mb-6">
        <label className="text-xs font-medium text-[#1A2535]/50 uppercase tracking-widest">
          Participantes
        </label>
        <AnimatePresence>
          {names.map((name, i) => (
            <motion.div
              key={i}
              initial={{ opacity: 0, x: -8 }}
              animate={{ opacity: 1, x: 0 }}
              exit={{ opacity: 0, x: 8, height: 0 }}
              transition={{ duration: 0.2 }}
              className="flex gap-2"
            >
              <input
                value={name}
                onChange={(e) => updateName(i, e.target.value)}
                onFocus={() => setFocusIdx(i)}
                onBlur={() => setFocusIdx(null)}
                placeholder={`Jugador ${i + 1}`}
                maxLength={20}
                className={`flex-1 bg-[#E8E0D0] border rounded-xl px-4 py-3 text-[#1A2535] text-sm placeholder:text-[#1A2535]/25 focus:outline-none transition-all duration-200 ${
                  focusIdx === i
                    ? "border-[#6BB5B5] bg-[#DDD4C2]"
                    : "border-[#D0C6B2]"
                }`}
              />
              {names.length > 2 && (
                <button
                  onClick={() => removePlayer(i)}
                  className="w-11 h-11 rounded-xl bg-[#E8E0D0] border border-[#D0C6B2] text-[#1A2535]/30 hover:text-[#D4888A] hover:border-[#D4888A]/40 transition-all duration-200 flex items-center justify-center"
                >
                  <svg width="14" height="14" viewBox="0 0 14 14" fill="none">
                    <line x1="2" y1="7" x2="12" y2="7" stroke="currentColor" strokeWidth="2" strokeLinecap="round" />
                  </svg>
                </button>
              )}
            </motion.div>
          ))}
        </AnimatePresence>

        {names.length < 8 && (
          <button
            onClick={addPlayer}
            className="w-full py-2.5 rounded-xl border border-dashed border-[#D0C6B2] text-[#1A2535]/40 text-sm hover:border-[#6BB5B5]/50 hover:text-[#6BB5B5] transition-all duration-200"
          >
            + Agregar jugador
          </button>
        )}
      </div>

      {/* Spice toggle */}
      <div
        onClick={() => setSpice(!spice)}
        className={`w-full max-w-sm flex items-center gap-3 p-4 rounded-xl border cursor-pointer transition-all duration-200 mb-8 ${
          spice
            ? "bg-[#E8906A]/8 border-[#E8906A]/30"
            : "bg-[#E8E0D0] border-[#D0C6B2]"
        }`}
      >
        <div className={`w-10 h-6 rounded-full flex items-center transition-all duration-200 px-0.5 ${spice ? "bg-[#E8906A]" : "bg-[#D0C6B2]"}`}>
          <motion.div
            className="w-5 h-5 rounded-full bg-white shadow-sm"
            animate={{ x: spice ? 16 : 0 }}
            transition={{ type: "spring", stiffness: 400, damping: 30 }}
          />
        </div>
        <div>
          <p className={`text-sm font-medium transition-colors ${spice ? "text-[#CC7050]" : "text-[#1A2535]/60"}`}>
            Incluir categoría Sin Filtro
          </p>
          <p className="text-xs text-[#1A2535]/35">Solo para mayores de 18 años</p>
        </div>
      </div>

      {/* Start button */}
      <motion.button
        onClick={start}
        disabled={validPlayers.length < 2}
        whileTap={{ scale: 0.97 }}
        className={`w-full max-w-sm py-4 rounded-xl font-semibold text-sm transition-all duration-200 ${
          validPlayers.length >= 2
            ? "bg-[#6BB5B5] hover:bg-[#4A9494] text-white shadow-lg shadow-[#6BB5B5]/25"
            : "bg-[#D0C6B2] text-[#1A2535]/25 cursor-not-allowed"
        }`}
      >
        Comenzar
      </motion.button>
    </motion.div>
  );
}
