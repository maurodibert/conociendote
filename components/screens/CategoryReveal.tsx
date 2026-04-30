"use client";

import { AnimatePresence, motion } from "framer-motion";
import { useState } from "react";
import { useGame } from "@/lib/GameContext";
import { CATEGORY_ICONS } from "@/components/icons/IsometricIcons";
import { Category } from "@/lib/types";

export default function CategoryReveal() {
  const { state, categories, dispatch, getRandomCategory } = useGame();
  const currentPlayer = state.players[state.currentPlayerIndex];
  const [winner, setWinner] = useState<Category | null>(null);
  const [choosingMode, setChoosingMode] = useState(false);
  const [hoveredId, setHoveredId] = useState<string | null>(null);

  const cols = 3;

  function getGridPos(index: number) {
    const col = index % cols;
    const row = Math.floor(index / cols);
    const totalRows = Math.ceil(categories.length / cols);
    const tilesInRow = Math.min(cols, categories.length - row * cols);
    const colShift = (cols - tilesInRow) / 2;
    const gridX = (col + colShift - (cols - 1) / 2) * 130;
    const gridY = (row - (totalRows - 1) / 2) * 120;
    return { x: gridX, y: gridY };
  }

  function handleDiscover() {
    setWinner(getRandomCategory());
    setChoosingMode(false);
    setHoveredId(null);
  }

  function handleTileTap(cat: Category) {
    if (!choosingMode) return;
    setWinner(cat);
    // stay in choosingMode so user can tap another to change
  }

  function confirmCategory() {
    if (!winner) return;
    dispatch({ type: "SELECT_CATEGORY", category: winner });
  }

  function cancelChoosing() {
    setChoosingMode(false);
    setWinner(null);
    setHoveredId(null);
  }

  return (
    <div className="relative flex flex-col items-center justify-center min-h-full overflow-hidden select-none">
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
          const isSelected = winner?.id === cat.id;
          const isHovered = hoveredId === cat.id && choosingMode && !isSelected;
          const { x, y } = getGridPos(i);
          const floatDelay = (i * 0.37) % 2.5;
          const floatDuration = 2.2 + (i * 0.19) % 1.2;

          return (
            <motion.div
              key={cat.id}
              className="absolute"
              style={{ cursor: choosingMode ? "pointer" : "default", zIndex: isSelected ? 10 : 1 }}
              animate={{ x, y }}
              transition={{ type: "spring", stiffness: 180, damping: 22, delay: i * 0.06 }}
              onClick={() => handleTileTap(cat)}
              onMouseEnter={() => choosingMode && !isSelected && setHoveredId(cat.id)}
              onMouseLeave={() => setHoveredId(null)}
            >
              {/* Floating tile */}
              <motion.div
                animate={{ y: [0, -7, 0] }}
                transition={{
                  duration: floatDuration,
                  delay: floatDelay,
                  repeat: Infinity,
                  ease: "easeInOut",
                }}
              >
                <div className="relative flex flex-col items-center gap-1.5 p-2">
                  <motion.div
                    className="rounded-xl p-2.5 relative overflow-hidden"
                    animate={{
                      boxShadow: isSelected
                        ? [`0 0 0 2.5px ${cat.color}, 0 0 0 4.5px ${cat.color}40`, `0 0 0 2.5px ${cat.color}CC, 0 0 0 5px ${cat.color}20`, `0 0 0 2.5px ${cat.color}, 0 0 0 4.5px ${cat.color}40`]
                        : isHovered
                        ? `0 0 0 2px ${cat.color}90`
                        : `0 0 0 1px ${cat.color}45`,
                    }}
                    transition={
                      isSelected
                        ? { duration: 1.8, repeat: Infinity, ease: "easeInOut" }
                        : { duration: 0.2 }
                    }
                    style={{ backgroundColor: `${cat.color}18` }}
                  >
                    {Icon && <Icon color={cat.color} shadowColor={cat.shadowColor} size={50} />}
                  </motion.div>
                  <span
                    className="text-xs font-medium text-center leading-tight"
                    style={{
                      maxWidth: 70,
                      color: isSelected ? cat.color : "#1A2535A8",
                      transition: "color 0.3s ease",
                    }}
                  >
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

          {/* No winner, not choosing */}
          {!winner && !choosingMode && (
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
                onClick={handleDiscover}
                whileTap={{ scale: 0.97 }}
                className="w-full py-4 rounded-xl font-semibold text-sm bg-[#6BB5B5] hover:bg-[#4A9494] text-white shadow-lg shadow-[#6BB5B5]/25 transition-colors"
              >
                Descubrir categoría
              </motion.button>
            </motion.div>
          )}

          {/* Choosing mode: no selection yet */}
          {choosingMode && !winner && (
            <motion.div
              key="choosing-empty"
              initial={{ opacity: 0, y: 12 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0 }}
              className="text-center space-y-3"
            >
              <p className="text-sm text-[#1A2535]/55">Tocá la categoría que querés</p>
              <button onClick={cancelChoosing} className="text-xs text-[#1A2535]/30 underline">
                Cancelar
              </button>
            </motion.div>
          )}

          {/* Winner selected (random or chosen) */}
          {winner && (
            <motion.div
              key="winner"
              initial={{ opacity: 0, y: 16 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0 }}
              transition={{ delay: 0.1 }}
              className="space-y-2"
            >
              <p className="text-center text-xs text-[#1A2535]/35 font-light">
                {choosingMode ? "Tocá otra para cambiarla" : "Categoría"}
              </p>
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
              {choosingMode && (
                <button onClick={cancelChoosing} className="w-full text-xs text-[#1A2535]/30 py-1">
                  Cancelar
                </button>
              )}
            </motion.div>
          )}

        </AnimatePresence>
      </div>
    </div>
  );
}
