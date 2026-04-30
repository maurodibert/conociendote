"use client";

interface IconProps {
  color: string;
  shadowColor: string;
  size?: number;
}

// Shared isometric cube base helper
function IsoCube({ color, shadowColor, size = 48, top }: IconProps & { top: React.ReactNode }) {
  const s = size;
  const h = s * 0.5;
  const q = s * 0.25;
  return (
    <svg width={s * 1.4} height={s * 1.2} viewBox={`0 0 ${s * 1.4} ${s * 1.2}`} fill="none">
      {/* Top face */}
      <polygon
        points={`${s * 0.7},${q * 0.5} ${s * 1.35},${q * 1.5} ${s * 0.7},${q * 2.5} ${s * 0.05},${q * 1.5}`}
        fill={color}
        stroke={shadowColor}
        strokeWidth="0.5"
        opacity="0.95"
      />
      {/* Left face */}
      <polygon
        points={`${s * 0.05},${q * 1.5} ${s * 0.7},${q * 2.5} ${s * 0.7},${q * 4.5} ${s * 0.05},${q * 3.5}`}
        fill={shadowColor}
        opacity="0.55"
      />
      {/* Right face */}
      <polygon
        points={`${s * 0.7},${q * 2.5} ${s * 1.35},${q * 1.5} ${s * 1.35},${q * 3.5} ${s * 0.7},${q * 4.5}`}
        fill={shadowColor}
        opacity="0.35"
      />
      {/* Icon on top face - centered */}
      <g transform={`translate(${s * 0.7}, ${q * 1.5})`}>{top}</g>
    </svg>
  );
}

export function InfanciaIcon({ color, shadowColor, size = 48 }: IconProps) {
  // Star / childhood toy
  return (
    <IsoCube color={color} shadowColor={shadowColor} size={size} top={
      <g>
        <polygon points="0,-9 2.5,-3 9,-3 4,1 6,8 0,4 -6,8 -4,1 -9,-3 -2.5,-3"
          fill="white" opacity="0.9" />
      </g>
    } />
  );
}

export function FuturoIcon({ color, shadowColor, size = 48 }: IconProps) {
  // Triangle / mountain / pyramid
  return (
    <IsoCube color={color} shadowColor={shadowColor} size={size} top={
      <g>
        <polygon points="0,-10 9,6 -9,6" fill="white" opacity="0.9" />
        <polygon points="0,-5 4,1 -4,1" fill={color} opacity="0.6" />
      </g>
    } />
  );
}

export function AmorIcon({ color, shadowColor, size = 48 }: IconProps) {
  // Heart (geometric)
  return (
    <IsoCube color={color} shadowColor={shadowColor} size={size} top={
      <g>
        <path d="M0 8 C-10,-4 -14,-10 -7,-12 C-3,-14 0,-10 0,-8 C0,-10 3,-14 7,-12 C14,-10 10,-4 0,8Z"
          fill="white" opacity="0.9" />
      </g>
    } />
  );
}

export function FamiliaIcon({ color, shadowColor, size = 48 }: IconProps) {
  // House / home
  return (
    <IsoCube color={color} shadowColor={shadowColor} size={size} top={
      <g>
        <polygon points="0,-11 10,0 6,0 6,9 -6,9 -6,0 -10,0" fill="white" opacity="0.9" />
        <rect x="-3" y="3" width="6" height="6" fill={color} opacity="0.7" />
      </g>
    } />
  );
}

export function AmistadIcon({ color, shadowColor, size = 48 }: IconProps) {
  // Two circles (people)
  return (
    <IsoCube color={color} shadowColor={shadowColor} size={size} top={
      <g>
        <circle cx="-4" cy="-4" r="5" fill="white" opacity="0.9" />
        <circle cx="4" cy="-4" r="5" fill="white" opacity="0.9" />
        <path d="M-9,4 Q-4,10 0,10 Q4,10 9,4" stroke="white" strokeWidth="1.5" fill="none" opacity="0.9" />
      </g>
    } />
  );
}

export function ExsIcon({ color, shadowColor, size = 48 }: IconProps) {
  // Broken chain / two squares with gap
  return (
    <IsoCube color={color} shadowColor={shadowColor} size={size} top={
      <g>
        <rect x="-10" y="-4" width="7" height="7" rx="1.5" fill="white" opacity="0.9" />
        <rect x="3" y="-4" width="7" height="7" rx="1.5" fill="white" opacity="0.9" />
        <line x1="-3" y1="-1" x2="3" y2="-1" stroke="white" strokeWidth="1.5" strokeDasharray="2 2" opacity="0.7" />
      </g>
    } />
  );
}

export function PersonalidadIcon({ color, shadowColor, size = 48 }: IconProps) {
  // Diamond / gem
  return (
    <IsoCube color={color} shadowColor={shadowColor} size={size} top={
      <g>
        <polygon points="0,-11 9,0 0,11 -9,0" fill="white" opacity="0.9" />
        <polygon points="0,-5 4,0 0,5 -4,0" fill={color} opacity="0.6" />
      </g>
    } />
  );
}

export function MiedosIcon({ color, shadowColor, size = 48 }: IconProps) {
  // Eye / shadow eye
  return (
    <IsoCube color={color} shadowColor={shadowColor} size={size} top={
      <g>
        <path d="M-10,0 Q0,-8 10,0 Q0,8 -10,0Z" fill="white" opacity="0.9" />
        <circle cx="0" cy="0" r="3.5" fill={shadowColor} opacity="0.8" />
        <circle cx="1" cy="-1" r="1" fill="white" opacity="0.8" />
      </g>
    } />
  );
}

export function LogrosIcon({ color, shadowColor, size = 48 }: IconProps) {
  // Trophy / cup
  return (
    <IsoCube color={color} shadowColor={shadowColor} size={size} top={
      <g>
        <path d="M-6,-9 L6,-9 L6,0 Q6,7 0,9 Q-6,7 -6,0 Z" fill="white" opacity="0.9" />
        <path d="M-6,-6 Q-12,-2 -10,4 Q-6,5 -6,0" stroke="white" strokeWidth="1.5" fill="none" opacity="0.8" />
        <path d="M6,-6 Q12,-2 10,4 Q6,5 6,0" stroke="white" strokeWidth="1.5" fill="none" opacity="0.8" />
        <rect x="-3" y="9" width="6" height="2" fill="white" opacity="0.7" />
      </g>
    } />
  );
}

export function SinFiltroIcon({ color, shadowColor, size = 48 }: IconProps) {
  // Flame
  return (
    <IsoCube color={color} shadowColor={shadowColor} size={size} top={
      <g>
        <path d="M0,10 C-8,4 -9,-2 -4,-8 C-2,-2 0,0 0,0 C0,-4 2,-8 4,-12 C8,-4 10,2 6,8 C8,4 6,0 4,2 C8,6 6,10 0,10Z"
          fill="white" opacity="0.9" />
      </g>
    } />
  );
}

export const CATEGORY_ICONS: Record<string, React.FC<IconProps>> = {
  infancia: InfanciaIcon,
  futuro: FuturoIcon,
  amor: AmorIcon,
  familia: FamiliaIcon,
  amistades: AmistadIcon,
  exs: ExsIcon,
  personalidad: PersonalidadIcon,
  miedos: MiedosIcon,
  logros: LogrosIcon,
  sinFiltro: SinFiltroIcon,
};
