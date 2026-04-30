"use client";

import { AnimatePresence, motion } from "framer-motion";
import { useCallback, useEffect, useRef, useState } from "react";
import { useGame } from "@/lib/GameContext";
import { CATEGORY_ICONS } from "@/components/icons/IsometricIcons";
import { Category } from "@/lib/types";

type Phase = "idle" | "shuffle" | "converging" | "revealed";

interface TilePos {
  x: number;
  y: number;
  rotate: number;
  scale: number;
}

export default function CategoryReveal() {
  const { state, categories, dispatch, getRandomCategory } = useGame();
  const currentPlayer = state.players[state.currentPlayerIndex];
  const [phase, setPhase] = useState<Phase>("idle");
  const [winner, setWinner] = useState<Category | null>(null);
  const [winnerIndex, setWinnerIndex] = useState<number | null>(null);
  const [choosingMode, setChoosingMode] = useState(false);
  const [dims, setDims] = useState({ w: 375, h: 667 });
  const [shufflePositions, setShufflePositions] = useState<TilePos[]>([]);
  const [exitPositions, setExitPositions] = useState<TilePos[]>([]);
  const containerRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    function measure() {
      if (containerRef.current) {
        setDims({ w: containerRef.current.offsetWidth, h: containerRef.current.offsetHeight });
      }
    }
    measure();
    window.addEventListener("resize", measure);
    return () => window.removeEventListener("resize", measure);
  }, []);

  const startReveal = useCallback(() => {
    if (phase !== "idle" && phase !== "revealed") return;
    setWinner(null);
    setWinnerIndex(null);

    // Pre-compute stable random positions for each tile
    const shuffled = categories.map(() => ({
      x: (Math.random() - 0.5) * dims.w * 0.75,
      y: (Math.random() - 0.5) * dims.h * 0.55,
      rotate: (Math.random() - 0.5) * 60,
      scale: 0.5 + Math.random() * 0.6,
    }));
    setShufflePositions(shuffled);
    setPhase("shuffle");

    setTimeout(() => {
      const chosen = getRandomCategory();
      const idx = categories.findIndex((c) => c.id === chosen.id);

      const exits = categories.map((_, i) =>
        i === idx
          ? { x: 0, y: 0, rotate: 0, scale: 1 }
          : {
              x: (Math.random() - 0.5) * dims.w * 2,
              y: dims.h * 0.8 + Math.random() * 200,
              rotate: (Math.random() - 0.5) * 90,
              scale: 0,
            }
      );
      setExitPositions(exits);
      setWinner(chosen);
      setWinnerIndex(idx);
      setPhase("converging");

      setTimeout(() => setPhase("revealed"), 1200);
    }, 1800);
  }, [phase, getRandomCategory, categories, dims]);

  const handleSelectCategory = useCallback(
    (cat: Category) => {
      if (!choosingMode) return;
      setChoosingMode(false);
      setWinner(cat);
      setWinnerIndex(categories.findIndex((c) => c.id === cat.id));
      setExitPositions([]);
      setPhase("revealed");
    },
    [choosingMode, categories]
  );

  function confirmCategory() {
    if (!winner) return;
    dispatch({ type: "SELECT_CATEGORY", category: winner });
  }

  function getAnimate(index: number): { x: number; y: number; rotate: number; scale: number; opacity: number } {
    const isWinner = index === winnerIndex;
    const cols = 3;
    const col = index % cols;
    const row = Math.floor(index / cols);
    const totalRows = Math.ceil(categories.length / cols);
    const tilesInRow = Math.min(cols, categories.length - row * cols);
    const colShift = (cols - tilesInRow) / 2; // center last incomplete row
    const gridX = (col + colShift - (cols - 1) / 2) * 130;
    const gridY = (row - (totalRows - 1) / 2) * 120;

    if (phase === "idle" || (phase === "revealed" && exitPositions.length === 0)) {
      if (phase === "revealed" && isWinner)
        return { x: 0, y: -20, rotate: 0, scale: 1.4, opacity: 1 };
      return { x: gridX, y: gridY, rotate: 0, scale: 1, opacity: 1 };
    }
    if (phase === "shuffle" && shufflePositions[index]) {
      const p = shufflePositions[index];
      return { x: p.x, y: p.y, rotate: p.rotate, scale: p.scale, opacity: 0.7 };
    }
    if (phase === "converging" && exitPositions[index]) {
      const p = exitPositions[index];
      if (isWinner) return { x: 0, y: 0, rotate: 0, scale: 1.2, opacity: 1 };
      return { x: p.x, y: p.y, rotate: p.rotate, scale: p.scale, opacity: 0 };
    }
    if (phase === "revealed") {
      if (isWinner) return { x: 0, y: -20, rotate: 0, scale: 1.4, opacity: 1 };
      const p = exitPositions[index];
      if (p) return { x: p.x, y: p.y, rotate: p.rotate, scale: p.scale, opacity: 0 };
    }
    return { x: gridX, y: gridY, rotate: 0, scale: 1, opacity: 1 };
  }

  function getTransition(index: number) {
    const isWinner = index === winnerIndex;
    if (phase === "shuffle")
      return { duration: 0.4, ease: "easeInOut" as const, delay: index * 0.04 };
    if (phase === "converging")
      return { duration: 0.65, ease: "easeOut" as const, delay: isWinner ? 0 : index * 0.02 };
    if (phase === "revealed")
      return { duration: 0.35, ease: "easeOut" as const };
    return { type: "spring" as const, stiffness: 180, damping: 22, delay: index * 0.06 };
  }

  return (
    <div ref={containerRef} className="relative flex flex-col items-center justify-center min-h-full overflow-hidden select-none">
      {/* Header */}
      <div className="absolute top-0 left-0 right-0 flex items-center justify-between px-5 py-4 border-b border-[#D0C6B2] bg-[#F2ECE4]/90 backdrop-blur-sm z-20">
        <span className="text-sm font-medium text-[#1A2535]/50">Ronda {state.round}</span>
        <span className="text-sm font-semibold text-[#1A2535]">{currentPlayer.name}</span>
        <div className="flex items-center gap-1.5">
          <span className="text-xs text-[#1A2535]/40">pts</span>
          <span className="text-sm font-bold text-[#6BB5B5]">{currentPlayer.points}</span>
        </div>
      </div>

      {/* Tiles */}
      <div className="relative flex items-center justify-center w-full flex-1 pt-14 pb-32">
        {categories.map((cat, i) => {
          const Icon = CATEGORY_ICONS[cat.id];
          const isWinner = i === winnerIndex;

          const floatDelay = (i * 0.37) % 2.5;
          const floatDuration = 2.2 + (i * 0.19) % 1.2;

          return (
            <motion.div
              key={cat.id}
              className="absolute cursor-pointer"
              style={{ zIndex: isWinner && phase !== "idle" ? 10 : 1 }}
              animate={getAnimate(i)}
              transition={getTransition(i)}
              onClick={() => choosingMode && handleSelectCategory(cat)}
              whileHover={choosingMode ? { scale: 1.08, zIndex: 20 } : undefined}
              whileTap={choosingMode ? { scale: 0.95 } : undefined}
            >
              {/* Inner float wrapper — only active in idle phase */}
              <motion.div
                animate={phase === "idle" || (phase === "revealed" && exitPositions.length === 0 && !isWinner)
                  ? { y: [0, -7, 0] }
                  : { y: 0 }}
                transition={{
                  duration: floatDuration,
                  delay: floatDelay,
                  repeat: Infinity,
                  ease: "easeInOut",
                }}
              >
              <div className="relative flex flex-col items-center gap-1.5 p-2">
                <div
                  className="rounded-xl p-2.5 border relative overflow-hidden"
                  style={{
                    backgroundColor: `${cat.color}18`,
                    borderColor: `${cat.color}45`,
                    boxShadow:
                      isWinner && (phase === "converging" || phase === "revealed")
                        ? `0 16px 48px ${cat.color}35`
                        : undefined,
                  }}
                >
                  {Icon && <Icon color={cat.color} shadowColor={cat.shadowColor} size={50} />}
                  {isWinner && (phase === "converging" || phase === "revealed") && (
                    <motion.div
                      className="absolute inset-0 rounded-xl"
                      style={{ backgroundColor: cat.color }}
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 0.1 }}
                    />
                  )}
                </div>
                <span className="text-xs font-medium text-center leading-tight text-[#1A2535]/65" style={{ maxWidth: 70 }}>
                  {cat.shortName}
                </span>
              </div>
              </motion.div>
            </motion.div>
          );
        })}
      </div>

      {/* Bottom panel */}
      <div className="absolute bottom-0 left-0 right-0 px-5 pb-8 pt-6 bg-gradient-to-t from-[#F2ECE4] via-[#F2ECE4]/95 to-transparent z-20">
        <AnimatePresence mode="wait">
          {phase === "idle" && !choosingMode && (
            <motion.div
              key="idle"
              initial={{ opacity: 0, y: 12 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -8 }}
              className="space-y-3"
            >
              {state.canChooseCategory && (
                <button
                  onClick={() => setChoosingMode(true)}
                  className="w-full py-3 rounded-xl text-sm font-medium bg-[#E8E0D0] border border-[#D0C6B2] text-[#1A2535]/55 hover:bg-[#DDD4C2] transition-all"
                >
                  Elegir categoría
                </button>
              )}
              <motion.button
                onClick={startReveal}
                whileTap={{ scale: 0.97 }}
                className="w-full py-4 rounded-xl font-semibold text-sm bg-[#6BB5B5] hover:bg-[#4A9494] text-white shadow-lg shadow-[#6BB5B5]/25 transition-colors"
              >
                Descubrir categoría
              </motion.button>
            </motion.div>
          )}

          {phase === "shuffle" && (
            <motion.div
              key="shuffle"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="text-center py-2"
            >
              <p className="text-[#1A2535]/35 text-sm font-light tracking-wide">Mezclando...</p>
            </motion.div>
          )}

          {phase === "revealed" && winner && (
            <motion.div
              key="revealed"
              initial={{ opacity: 0, y: 16 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0 }}
              transition={{ delay: 0.15 }}
              className="space-y-2"
            >
              <p className="text-center text-xs text-[#1A2535]/35 font-light">Categoría</p>
              <p className="text-center text-2xl font-bold tracking-tight" style={{ color: winner.color }}>
                {winner.name}
              </p>
              <motion.button
                onClick={confirmCategory}
                whileTap={{ scale: 0.97 }}
                className="w-full py-4 mt-3 rounded-xl font-semibold text-sm text-white shadow-lg transition-colors"
                style={{ backgroundColor: winner.color, boxShadow: `0 8px 24px ${winner.color}40` }}
              >
                Continuar
              </motion.button>
            </motion.div>
          )}

          {choosingMode && (
            <motion.div
              key="choosing"
              initial={{ opacity: 0, y: 12 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0 }}
              className="text-center space-y-3"
            >
              <p className="text-sm text-[#1A2535]/55">Tocá la categoría que querés</p>
              <button onClick={() => setChoosingMode(false)} className="text-xs text-[#1A2535]/30 underline">
                Cancelar
              </button>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </div>
  );
}
