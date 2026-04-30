import { GameProvider } from "@/lib/GameContext";
import GameApp from "@/components/GameApp";
import { Category } from "@/lib/types";
import questionsData from "@/data/questions.json";

export default function Home() {
  const categories = questionsData.categories as Category[];

  return (
    <GameProvider categories={categories}>
      <GameApp />
    </GameProvider>
  );
}
