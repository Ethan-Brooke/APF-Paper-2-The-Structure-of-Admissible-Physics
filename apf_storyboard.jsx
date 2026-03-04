import { useState, useEffect } from "react";

// ─── Color palette ────────────────────────────────────────────────────────────
const C = {
  bg:       "#07090f",
  panel:    "#0c1120",
  border:   "#1a2540",
  dim:      "#1e2d4a",
  muted:    "#2a3d5c",
  text:     "#c8d6e8",
  faint:    "#4a6080",
  accent1:  "#4f9cf0",   // spin / blue
  accent2:  "#f0b44f",   // position / gold
  surplus:  "#e05555",   // Δ / interference
  abelian:  "#4ec994",   // abelian
  nonabl:   "#c975f0",   // non-abelian
  white:    "#f0f4fc",
};

// ─── Shared drawing primitives ────────────────────────────────────────────────
const ArrowDef = () => (
  <defs>
    <marker id="arr-blue" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill={C.accent1} />
    </marker>
    <marker id="arr-gold" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill={C.accent2} />
    </marker>
    <marker id="arr-red" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill={C.surplus} />
    </marker>
    <marker id="arr-white" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill={C.white} />
    </marker>
    <marker id="arr-green" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill={C.abelian} />
    </marker>
    <marker id="arr-purple" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z" fill={C.nonabl} />
    </marker>
  </defs>
);

// ─── Panel 1: The hydrogen atom ───────────────────────────────────────────────
function Panel1() {
  // Spin is genuinely binary: exactly two states, one channel, κ=2 applies directly.
  // Position is NOT binary: the electron is described by a continuous wavefunction —
  // a probability cloud spread across the orbital. Enforcing position means
  // committing binary distinctions from a stack: is it in this half? this quarter?
  // The cloud shows the current enforcement state of that stack.
  // We show the electron embedded in the orbital cloud, not as a point on a track.

  const cx = 220, cy = 148;

  return (
    <svg viewBox="0 0 520 300" style={{width:"100%", height:"100%"}}>
      <ArrowDef />
      <defs>
        {/* Radial gradient for orbital probability cloud */}
        <radialGradient id="orbital" cx="50%" cy="50%" r="50%">
          <stop offset="0%"   stopColor={C.accent2} stopOpacity="0.35" />
          <stop offset="40%"  stopColor={C.accent2} stopOpacity="0.18" />
          <stop offset="70%"  stopColor={C.accent2} stopOpacity="0.07" />
          <stop offset="100%" stopColor={C.accent2} stopOpacity="0" />
        </radialGradient>
      </defs>

      {/* Orbital cloud — 1s-like probability distribution */}
      <ellipse cx={cx} cy={cy} rx={88} ry={80}
        fill="url(#orbital)" />
      {/* Second shell ring to suggest density contours */}
      <ellipse cx={cx} cy={cy} rx={52} ry={48}
        fill="none" stroke={C.accent2} strokeWidth={0.5} opacity={0.3} />
      <ellipse cx={cx} cy={cy} rx={76} ry={70}
        fill="none" stroke={C.accent2} strokeWidth={0.4} opacity={0.15} />

      {/* Nucleus */}
      <circle cx={cx} cy={cy} r={10} fill={C.muted} stroke={C.accent1} strokeWidth={1.5} />
      <text x={cx} y={cy+4} textAnchor="middle" fill={C.accent1} fontSize={9} fontFamily="serif">p⁺</text>

      {/* Electron — inside the cloud, not on a track */}
      <circle cx={cx+46} cy={cy-28} r={7} fill={C.accent2} opacity={0.9} />
      <text x={cx+46} y={cy-24} textAnchor="middle" fill={C.bg} fontSize={8} fontFamily="monospace">e⁻</text>

      {/* Spin arrow — the one genuinely binary observable */}
      <line x1={cx+46} y1={cy-42} x2={cx+46} y2={cy-56} stroke={C.accent1} strokeWidth={2}
        markerEnd="url(#arr-blue)" />

      {/* Spin label */}
      <rect x={54} y={68} width={136} height={46} rx={3}
        fill={C.panel} stroke={C.accent1} strokeWidth={1} opacity={0.95} />
      <text x={122} y={84} textAnchor="middle" fill={C.accent1} fontSize={10} fontFamily="monospace">
        spin: ↑ or ↓
      </text>
      <text x={122} y={98} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        one binary channel
      </text>
      <text x={122} y={110} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        κ = 2, exactly
      </text>

      {/* Position label — continuous stack */}
      <rect x={326} y={156} width={172} height={58} rx={3}
        fill={C.panel} stroke={C.accent2} strokeWidth={1} opacity={0.95} />
      <text x={412} y={172} textAnchor="middle" fill={C.accent2} fontSize={10} fontFamily="monospace">
        position: where in
      </text>
      <text x={412} y={186} textAnchor="middle" fill={C.accent2} fontSize={10} fontFamily="monospace">
        the orbital?
      </text>
      <text x={412} y={200} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        a stack of binary distinctions
      </text>
      <text x={412} y={210} textAnchor="middle" fill={C.faint} fontSize={8} fontFamily="monospace">
        continuous · many channels
      </text>

      {/* Arrows from labels */}
      <line x1={190} y1={96} x2={214} y2={136} stroke={C.accent1} strokeWidth={0.8}
        strokeDasharray="2 2" opacity={0.5} />
      <line x1={330} y1={175} x2={280} y2={158} stroke={C.accent2} strokeWidth={0.8}
        strokeDasharray="2 2" opacity={0.5} />

      {/* Context note */}
      <text x={260} y={272} textAnchor="middle" fill={C.faint} fontSize={10} fontFamily="monospace">
        drifting in deep space · vast capacity headroom · no stress
      </text>
    </svg>
  );
}

// ─── Panel 2: The shared pool ─────────────────────────────────────────────────
function Panel2() {
  // The pool is local to this interface — a proper, bounded subset of
  // whatever the global structure is. We draw it as a fenced region with
  // no count attached. The only claim: it has a wall (finite) and both
  // tasks draw from the same side of it.
  //
  // Channels shown are loosely suggestive of EW-relevant ones for an
  // electron: a few SU(2) channels, a U(1) channel, some fermion channels.
  // They are unlabelled — the point is the shared boundary, not the count.

  const channelDots = [
    // roughly two rows, irregular spacing to avoid grid-implies-count reading
    {x:152,y:108},{x:182,y:104},{x:212,y:110},{x:240,y:106},{x:268,y:108},
    {x:296,y:104},{x:324,y:109},{x:352,y:106},{x:376,y:110},
    {x:162,y:134},{x:194,y:130},{x:224,y:136},{x:254,y:132},{x:282,y:134},
    {x:310,y:130},{x:338,y:135},{x:364,y:132},
  ];

  return (
    <svg viewBox="0 0 520 300" style={{width:"100%", height:"100%"}}>
      <ArrowDef />

      {/* The local interface boundary — a wall with visible edges */}
      <rect x={132} y={86} width={270} height={76} rx={6}
        fill={C.dim} stroke={C.border} strokeWidth={2} />

      {/* Label: local, no count */}
      <text x={267} y={78} textAnchor="middle"
        fill={C.faint} fontSize={10} fontFamily="monospace">
        local enforcement pool at this interface · C(Γ) &lt; ∞
      </text>

      {/* Channel dots — unlabelled, irregular, just "some finite set" */}
      {channelDots.map((d, i) => (
        <circle key={i} cx={d.x} cy={d.y} r={7}
          fill={C.muted} stroke={C.border} strokeWidth={1} />
      ))}

      {/* Explicit "not all 61" annotation */}
      <text x={267} y={174} textAnchor="middle"
        fill={C.faint} fontSize={9} fontFamily="monospace">
        a local subset — not the global structure
      </text>

      {/* Spin task */}
      <rect x={38} y={196} width={90} height={52} rx={3}
        fill={C.panel} stroke={C.accent1} strokeWidth={1.5} />
      <text x={83} y={215} textAnchor="middle" fill={C.accent1} fontSize={11} fontFamily="monospace">spin</text>
      <text x={83} y={229} textAnchor="middle" fill={C.accent1} fontSize={11} fontFamily="monospace">task</text>
      <text x={83} y={241} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">draws channels</text>

      {/* Position task */}
      <rect x={382} y={192} width={112} height={60} rx={3}
        fill={C.panel} stroke={C.accent2} strokeWidth={1.5} />
      <text x={438} y={210} textAnchor="middle" fill={C.accent2} fontSize={11} fontFamily="monospace">position</text>
      <text x={438} y={224} textAnchor="middle" fill={C.accent2} fontSize={11} fontFamily="monospace">stack</text>
      <text x={438} y={238} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">many channels</text>
      <text x={438} y={248} textAnchor="middle" fill={C.faint} fontSize={8} fontFamily="monospace">continuous</text>

      {/* Both arrows converge on the pool */}
      <line x1={128} y1={210} x2={192} y2={156} stroke={C.accent1} strokeWidth={1.5}
        markerEnd="url(#arr-blue)" />
      <line x1={394} y1={218} x2={340} y2={158} stroke={C.accent2} strokeWidth={1.5}
        markerEnd="url(#arr-gold)" />

      {/* Key insight */}
      <rect x={138} y={256} width={246} height={30} rx={3}
        fill={C.bg} stroke={C.border} strokeWidth={1} />
      <text x={261} y={268} textAnchor="middle" fill={C.text} fontSize={10} fontFamily="monospace">
        one pool · no dedicated lanes
      </text>
      <text x={261} y={280} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        both tasks route through the same bounded set
      </text>
    </svg>
  );
}

// ─── Panel 3: Spin commits — channels partitioned ─────────────────────────────
function Panel3() {
  // Same irregular dots as panel 2, but now partitioned by the spin commitment.
  // Some dots colored spin-up (bright blue), some spin-down (dark blue),
  // the rest dimmed — available but reconfigured. No counts anywhere.
  // The point: the remaining channels are not the same channels as before.

  const upDots =   [{x:152,y:96},{x:182,y:92},{x:212,y:98},{x:240,y:94},{x:268,y:96}];
  const downDots = [{x:162,y:122},{x:194,y:118},{x:224,y:124},{x:254,y:120},{x:282,y:122}];
  const restDots = [{x:296,y:96},{x:324,y:100},{x:352,y:94},{x:376,y:98},
                    {x:310,y:120},{x:338,y:124},{x:364,y:118}];

  return (
    <svg viewBox="0 0 520 300" style={{width:"100%", height:"100%"}}>
      <ArrowDef />

      {/* Pool boundary — same wall as panel 2 */}
      <rect x={132} y={76} width={270} height={76} rx={6}
        fill={C.dim} stroke={C.border} strokeWidth={2} />

      {/* Spin-up camp — bright blue */}
      {upDots.map((d,i) => (
        <g key={`u${i}`}>
          <circle cx={d.x} cy={d.y} r={7} fill={C.accent1} stroke={C.accent1} strokeWidth={1} />
          <text x={d.x} y={d.y+4} textAnchor="middle" fill={C.bg} fontSize={8} fontFamily="serif">↑</text>
        </g>
      ))}

      {/* Spin-down camp — dark blue */}
      {downDots.map((d,i) => (
        <g key={`d${i}`}>
          <circle cx={d.x} cy={d.y} r={7} fill="#1a3a6a" stroke={C.accent1} strokeWidth={1} />
          <text x={d.x} y={d.y+4} textAnchor="middle" fill={C.accent1} fontSize={8} fontFamily="serif">↓</text>
        </g>
      ))}

      {/* Remaining — dimmed, reconfigured */}
      {restDots.map((d,i) => (
        <circle key={`r${i}`} cx={d.x} cy={d.y} r={7}
          fill={C.muted} stroke={C.border} strokeWidth={1} opacity={0.5} />
      ))}

      {/* Spin-camp bracket label */}
      <line x1={134} y1={162} x2={288} y2={162} stroke={C.accent1} strokeWidth={0.8} />
      <line x1={134} y1={158} x2={134} y2={165} stroke={C.accent1} strokeWidth={0.8} />
      <line x1={288} y1={158} x2={288} y2={165} stroke={C.accent1} strokeWidth={0.8} />
      <text x={211} y={174} textAnchor="middle" fill={C.accent1} fontSize={9} fontFamily="monospace">
        committed to spin
      </text>

      {/* Remaining bracket label */}
      <line x1={294} y1={162} x2={400} y2={162} stroke={C.faint} strokeWidth={0.8} />
      <line x1={294} y1={158} x2={294} y2={165} stroke={C.faint} strokeWidth={0.8} />
      <line x1={400} y1={158} x2={400} y2={165} stroke={C.faint} strokeWidth={0.8} />
      <text x={347} y={174} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        remain
      </text>

      {/* Key callout */}
      <rect x={80} y={194} width={360} height={72} rx={4}
        fill={C.panel} stroke={C.surplus} strokeWidth={1} />
      <text x={260} y={213} textAnchor="middle" fill={C.surplus} fontSize={11} fontFamily="monospace">
        the position stack operates in a rearranged
      </text>
      <text x={260} y={229} textAnchor="middle" fill={C.surplus} fontSize={11} fontFamily="monospace">
        landscape — not the one it would have found
      </text>
      <text x={260} y={245} textAnchor="middle" fill={C.text} fontSize={10} fontFamily="monospace">
        each binary question in the position stack
      </text>
      <text x={260} y={259} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        costs more — Δ grows as precision is pushed
      </text>
    </svg>
  );
}

// ─── Panel 4: The interference surplus Δ ─────────────────────────────────────
function Panel4() {
  // Bars are proportional — no specific numbers.
  // The budget line C(Γ) is shown as a vertical wall.
  // E(spin) and E(pos) each fit inside the wall.
  // E(both) = E(spin) + E(pos) + Δ pushes past it.
  const barH = 28;
  const barY0 = 72;
  const barGap = 50;
  const budgetX = 310; // where the wall sits
  const labelX = 80;
  const startX = 130;

  return (
    <svg viewBox="0 0 520 300" style={{width:"100%", height:"100%"}}>
      <ArrowDef />

      {/* E(spin) alone — fits */}
      <text x={labelX} y={barY0+18} fill={C.accent1} fontSize={11} fontFamily="monospace">E(spin)</text>
      <rect x={startX} y={barY0} width={150} height={barH} rx={2}
        fill={C.accent1} opacity={0.8} />

      {/* E(pos) alone — fits */}
      <text x={labelX} y={barY0+barGap+18} fill={C.accent2} fontSize={11} fontFamily="monospace">E(pos)</text>
      <rect x={startX} y={barY0+barGap} width={150} height={barH} rx={2}
        fill={C.accent2} opacity={0.8} />

      {/* E(both) — overflows */}
      <text x={labelX} y={barY0+2*barGap+18} fill={C.text} fontSize={11} fontFamily="monospace">E(both)</text>
      <rect x={startX} y={barY0+2*barGap} width={150} height={barH} rx={0}
        fill={C.accent1} opacity={0.7} />
      <rect x={startX+150} y={barY0+2*barGap} width={150} height={barH} rx={0}
        fill={C.accent2} opacity={0.7} />
      <rect x={startX+300} y={barY0+2*barGap} width={46} height={barH} rx={2}
        fill={C.surplus} opacity={0.9} />
      <text x={startX+323} y={barY0+2*barGap+18} textAnchor="middle"
        fill={C.white} fontSize={11} fontFamily="monospace">Δ</text>

      {/* Budget wall C(Γ) */}
      <line x1={budgetX} y1={barY0-16} x2={budgetX} y2={barY0+2*barGap+barH+8}
        stroke={C.faint} strokeWidth={1.5} strokeDasharray="4 3" />
      <text x={budgetX+4} y={barY0-6} fill={C.faint} fontSize={9} fontFamily="monospace">
        C(Γ)
      </text>

      {/* Fits markers */}
      <text x={budgetX+10} y={barY0+18} fill={C.abelian} fontSize={10} fontFamily="monospace">✓</text>
      <text x={budgetX+10} y={barY0+barGap+18} fill={C.abelian} fontSize={10} fontFamily="monospace">✓</text>

      {/* Overflow marker */}
      <text x={startX+352} y={barY0+2*barGap+18} fill={C.surplus} fontSize={10} fontFamily="monospace">✗</text>
      <line x1={startX+348} y1={barY0+2*barGap+8} x2={startX+362} y2={barY0+2*barGap+8}
        stroke={C.surplus} strokeWidth={1} markerEnd="url(#arr-red)" />

      {/* Equation box */}
      <rect x={368} y={barY0} width={136} height={130} rx={4}
        fill={C.panel} stroke={C.border} strokeWidth={1} />
      <text x={436} y={barY0+22} textAnchor="middle"
        fill={C.text} fontSize={11} fontFamily="monospace">E(A∪B) =</text>
      <text x={436} y={barY0+42} textAnchor="middle"
        fill={C.text} fontSize={11} fontFamily="monospace">E(A) + E(B)</text>
      <text x={436} y={barY0+62} textAnchor="middle"
        fill={C.surplus} fontSize={13} fontFamily="monospace">    + Δ</text>
      <line x1={386} y1={barY0+74} x2={496} y2={barY0+74}
        stroke={C.border} strokeWidth={0.8} />
      <text x={436} y={barY0+90} textAnchor="middle"
        fill={C.faint} fontSize={9} fontFamily="monospace">Δ &gt; 0 always</text>
      <text x={436} y={barY0+106} textAnchor="middle"
        fill={C.faint} fontSize={9} fontFamily="monospace">not a budget crisis</text>
      <text x={436} y={barY0+122} textAnchor="middle"
        fill={C.faint} fontSize={9} fontFamily="monospace">structural property</text>

      {/* Caption */}
      <text x={260} y={254} textAnchor="middle" fill={C.faint} fontSize={10} fontFamily="monospace">
        Δ is the cost of enforcing B in A's rearranged landscape
      </text>
      <text x={260} y={270} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        present at every scale · in every regime · regardless of headroom
      </text>
    </svg>
  );
}

// ─── Panel 5: Path dependence — order matters ─────────────────────────────────
function Panel5() {
  // Two paths: spin-then-position vs position-then-spin
  // Show that the result is different (non-abelian) vs same (abelian)
  return (
    <svg viewBox="0 0 520 300" style={{width:"100%", height:"100%"}}>
      <ArrowDef />

      {/* Left column: path A→B */}
      <text x={130} y={32} textAnchor="middle" fill={C.text} fontSize={11} fontFamily="monospace">
        spin first, then position
      </text>

      {/* Start state */}
      <rect x={80} y={44} width={100} height={30} rx={3}
        fill={C.dim} stroke={C.border} strokeWidth={1} />
      <text x={130} y={64} textAnchor="middle" fill={C.faint} fontSize={10} fontFamily="monospace">
        fresh pool
      </text>

      {/* Arrow: commit spin */}
      <line x1={130} y1={75} x2={130} y2={104} stroke={C.accent1} strokeWidth={1.5}
        markerEnd="url(#arr-blue)" />
      <text x={145} y={94} fill={C.accent1} fontSize={9} fontFamily="monospace">spin ↑</text>

      {/* After spin */}
      <rect x={80} y={106} width={100} height={30} rx={3}
        fill={C.panel} stroke={C.accent1} strokeWidth={1.2} />
      <text x={130} y={126} textAnchor="middle" fill={C.accent1} fontSize={9} fontFamily="monospace">
        spin-shaped pool
      </text>

      {/* Arrow: now commit position IN that context */}
      <line x1={130} y1={137} x2={130} y2={166} stroke={C.accent2} strokeWidth={1.5}
        markerEnd="url(#arr-gold)" />
      <text x={145} y={157} fill={C.accent2} fontSize={9} fontFamily="monospace">pos stack</text>

      {/* Final state A */}
      <rect x={68} y={168} width={124} height={36} rx={3}
        fill={C.panel} stroke={C.faint} strokeWidth={1} />
      <text x={130} y={183} textAnchor="middle" fill={C.text} fontSize={9} fontFamily="monospace">
        cost: E(spin) + E(pos)
      </text>
      <text x={130} y={197} textAnchor="middle" fill={C.surplus} fontSize={10} fontFamily="monospace">
        + Δ(pos|spin-context)
      </text>

      {/* Right column: path B→A */}
      <text x={390} y={32} textAnchor="middle" fill={C.text} fontSize={11} fontFamily="monospace">
        position first, then spin
      </text>

      <rect x={340} y={44} width={100} height={30} rx={3}
        fill={C.dim} stroke={C.border} strokeWidth={1} />
      <text x={390} y={64} textAnchor="middle" fill={C.faint} fontSize={10} fontFamily="monospace">
        fresh pool
      </text>

      <line x1={390} y1={75} x2={390} y2={104} stroke={C.accent2} strokeWidth={1.5}
        markerEnd="url(#arr-gold)" />
      <text x={405} y={94} fill={C.accent2} fontSize={9} fontFamily="monospace">pos stack</text>

      <rect x={340} y={106} width={100} height={30} rx={3}
        fill={C.panel} stroke={C.accent2} strokeWidth={1.2} />
      <text x={390} y={126} textAnchor="middle" fill={C.accent2} fontSize={9} fontFamily="monospace">
        pos-shaped pool
      </text>

      <line x1={390} y1={137} x2={390} y2={166} stroke={C.accent1} strokeWidth={1.5}
        markerEnd="url(#arr-blue)" />
      <text x={405} y={157} fill={C.accent1} fontSize={9} fontFamily="monospace">spin ↑</text>

      <rect x={328} y={168} width={124} height={36} rx={3}
        fill={C.panel} stroke={C.faint} strokeWidth={1} />
      <text x={390} y={183} textAnchor="middle" fill={C.text} fontSize={9} fontFamily="monospace">
        cost: E(pos) + E(spin)
      </text>
      <text x={390} y={197} textAnchor="middle" fill={C.surplus} fontSize={10} fontFamily="monospace">
        + Δ(spin|pos-context)
      </text>

      {/* Not equal sign in middle */}
      <text x={260} y={192} textAnchor="middle" fill={C.surplus} fontSize={28} fontFamily="serif">
        ≠
      </text>

      {/* Bottom: consequence */}
      <rect x={80} y={224} width={360} height={46} rx={4}
        fill={C.panel} stroke={C.nonabl} strokeWidth={1} />
      <text x={260} y={241} textAnchor="middle" fill={C.nonabl} fontSize={11} fontFamily="monospace">
        AB ≠ BA  ·  order matters
      </text>
      <text x={260} y={257} textAnchor="middle" fill={C.text} fontSize={10} fontFamily="monospace">
        this is noncommutativity — the operational origin of non-abelian structure
      </text>
      <text x={260} y={269} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        each commitment rearranges the context for what comes next
      </text>
    </svg>
  );
}

// ─── Panel 6: Non-closure — A fits, B fits, A+B overflows ─────────────────────
function Panel6() {
  // Same proportional approach as panel 4.
  // No specific numbers — the wall is C(Γ), bars are proportional.
  const bw = 200;
  const cx = 240;
  const wallX = cx - bw/2 + bw;  // right edge of a bar that "fits"

  return (
    <svg viewBox="0 0 520 300" style={{width:"100%", height:"100%"}}>
      <ArrowDef />

      {/* Non-closure label */}
      <rect x={148} y={10} width={226} height={22} rx={3}
        fill={C.bg} stroke={C.nonabl} strokeWidth={1} />
      <text x={261} y={25} textAnchor="middle" fill={C.nonabl} fontSize={11} fontFamily="monospace">
        non-closure: A ✓  B ✓  A+B ✗
      </text>

      {/* Budget wall — the only thing that matters about C(Γ) */}
      <line x1={wallX} y1={44} x2={wallX} y2={234}
        stroke={C.faint} strokeWidth={1.5} strokeDasharray="4 3" />
      <text x={wallX+4} y={54} fill={C.faint} fontSize={9} fontFamily="monospace">C(Γ)</text>

      {/* Spin alone — fits inside wall */}
      <text x={cx-bw/2-42} y={90} fill={C.accent1} fontSize={10} fontFamily="monospace">spin</text>
      <rect x={cx-bw/2} y={76} width={bw} height={30} rx={3}
        fill={C.accent1} opacity={0.75} />
      <text x={wallX+12} y={95} fill={C.abelian} fontSize={13} fontFamily="monospace">✓</text>

      {/* Position alone — fits inside wall */}
      <text x={cx-bw/2-38} y={140} fill={C.accent2} fontSize={10} fontFamily="monospace">pos</text>
      <rect x={cx-bw/2} y={126} width={bw} height={30} rx={3}
        fill={C.accent2} opacity={0.75} />
      <text x={wallX+12} y={145} fill={C.abelian} fontSize={13} fontFamily="monospace">✓</text>

      {/* Both together — spin + pos bars flush, then Δ breaks the wall */}
      <text x={cx-bw/2-44} y={193} fill={C.text} fontSize={10} fontFamily="monospace">both</text>
      <rect x={cx-bw/2} y={178} width={bw/2} height={30} rx={0}
        fill={C.accent1} opacity={0.7} />
      <rect x={cx-bw/2+bw/2} y={178} width={bw/2} height={30} rx={0}
        fill={C.accent2} opacity={0.7} />
      {/* Δ bursts past the wall */}
      <rect x={wallX} y={178} width={52} height={30} rx={2}
        fill={C.surplus} opacity={0.9} />
      <text x={wallX+26} y={197} textAnchor="middle"
        fill={C.white} fontSize={11} fontFamily="monospace">Δ</text>
      <text x={wallX+62} y={197} fill={C.surplus} fontSize={13} fontFamily="monospace">✗</text>

      {/* Arrow: overflow */}
      <line x1={wallX+52} y1={193} x2={wallX+66} y2={193}
        stroke={C.surplus} strokeWidth={1.5} markerEnd="url(#arr-red)" />

      {/* Consequence */}
      <rect x={80} y={228} width={362} height={50} rx={4}
        fill={C.panel} stroke={C.border} strokeWidth={1} />
      <text x={261} y={246} textAnchor="middle" fill={C.text} fontSize={10} fontFamily="monospace">
        the interference surplus Δ pushes the joint cost past C(Γ)
      </text>
      <text x={261} y={262} textAnchor="middle" fill={C.text} fontSize={10} fontFamily="monospace">
        not because something went wrong — this is the normal structure
      </text>
      <text x={261} y={274} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        A1: capacity is finite · Δ &gt; 0: interference is structural · result: non-closure
      </text>
    </svg>
  );
}

// ─── Panel 7: Abelian (Δ=0) vs Non-abelian (Δ>0) — the key split ──────────────
function Panel7() {
  return (
    <svg viewBox="0 0 520 300" style={{width:"100%", height:"100%"}}>
      <ArrowDef />

      {/* Dividing line */}
      <line x1={260} y1={20} x2={260} y2={280} stroke={C.border} strokeWidth={1}
        strokeDasharray="3 4" />

      {/* ── LEFT: ABELIAN ── */}
      <text x={130} y={32} textAnchor="middle" fill={C.abelian} fontSize={12} fontFamily="monospace">
        abelian  (Δ = 0)
      </text>

      {/* Two paths that both reach same result */}
      {/* Start */}
      <circle cx={80} cy={70} r={8} fill={C.abelian} opacity={0.6} />
      {/* End */}
      <circle cx={210} cy={70} r={8} fill={C.abelian} opacity={0.6} />

      {/* Path 1: A then B (top) */}
      <path d="M 88 66 Q 145 44 202 66" fill="none" stroke={C.abelian} strokeWidth={1.5}
        markerEnd="url(#arr-green)" />
      <text x={145} y={50} textAnchor="middle" fill={C.abelian} fontSize={9} fontFamily="monospace">A then B</text>

      {/* Path 2: B then A (bottom) */}
      <path d="M 88 74 Q 145 96 202 74" fill="none" stroke={C.abelian} strokeWidth={1.5}
        markerEnd="url(#arr-green)" />
      <text x={145} y={100} textAnchor="middle" fill={C.abelian} fontSize={9} fontFamily="monospace">B then A</text>

      {/* = sign */}
      <text x={145} y={72} textAnchor="middle" fill={C.abelian} fontSize={14} fontFamily="serif">=</text>

      {/* What this means */}
      <rect x={34} y={116} width={196} height={76} rx={3}
        fill={C.panel} stroke={C.abelian} strokeWidth={0.8} />
      <text x={132} y={134} textAnchor="middle" fill={C.text} fontSize={9} fontFamily="monospace">
        first commitment doesn't
      </text>
      <text x={132} y={148} textAnchor="middle" fill={C.text} fontSize={9} fontFamily="monospace">
        rearrange the landscape
      </text>
      <text x={132} y={166} textAnchor="middle" fill={C.abelian} fontSize={10} fontFamily="monospace">
        Δ = 0 everywhere
      </text>
      <text x={132} y={182} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        no surplus · no exclusion
      </text>

      {/* Physics consequence */}
      <rect x={34} y={204} width={196} height={56} rx={3}
        fill={C.bg} stroke={C.faint} strokeWidth={0.8} />
      <text x={132} y={220} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        everything that individually fits
      </text>
      <text x={132} y={234} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        also jointly fits
      </text>
      <text x={132} y={250} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        no structure forced · no gauge group
      </text>

      {/* ── RIGHT: NON-ABELIAN ── */}
      <text x={390} y={32} textAnchor="middle" fill={C.nonabl} fontSize={12} fontFamily="monospace">
        non-abelian  (Δ &gt; 0)
      </text>

      <circle cx={280} cy={70} r={8} fill={C.nonabl} opacity={0.6} />

      {/* Two paths that reach DIFFERENT results */}
      <circle cx={390} cy={50} r={8} fill={C.nonabl} opacity={0.5} />
      <circle cx={390} cy={94} r={8} fill={C.nonabl} opacity={0.5} />

      <path d="M 288 64 Q 335 42 382 50" fill="none" stroke={C.nonabl} strokeWidth={1.5}
        markerEnd="url(#arr-purple)" />
      <text x={334} y={44} textAnchor="middle" fill={C.nonabl} fontSize={9} fontFamily="monospace">A then B</text>

      <path d="M 288 76 Q 335 98 382 94" fill="none" stroke={C.nonabl} strokeWidth={1.5}
        markerEnd="url(#arr-purple)" />
      <text x={334} y={106} textAnchor="middle" fill={C.nonabl} fontSize={9} fontFamily="monospace">B then A</text>

      {/* ≠ */}
      <text x={406} y={75} textAnchor="middle" fill={C.surplus} fontSize={18} fontFamily="serif">≠</text>

      <rect x={270} y={116} width={216} height={76} rx={3}
        fill={C.panel} stroke={C.nonabl} strokeWidth={0.8} />
      <text x={378} y={134} textAnchor="middle" fill={C.text} fontSize={9} fontFamily="monospace">
        first commitment rearranges
      </text>
      <text x={378} y={148} textAnchor="middle" fill={C.text} fontSize={9} fontFamily="monospace">
        the landscape for the second
      </text>
      <text x={378} y={166} textAnchor="middle" fill={C.nonabl} fontSize={10} fontFamily="monospace">
        Δ &gt; 0 always present
      </text>
      <text x={378} y={182} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        order matters · AB ≠ BA
      </text>

      <rect x={270} y={204} width={216} height={56} rx={3}
        fill={C.bg} stroke={C.nonabl} strokeWidth={0.8} />
      <text x={378} y={220} textAnchor="middle" fill={C.text} fontSize={9} fontFamily="monospace">
        some combinations overflow
      </text>
      <text x={378} y={234} textAnchor="middle" fill={C.text} fontSize={9} fontFamily="monospace">
        cheapest surviving combo persists
      </text>
      <text x={378} y={250} textAnchor="middle" fill={C.nonabl} fontSize={9} fontFamily="monospace">
        gauge group forced · structure emerges
      </text>
    </svg>
  );
}

// ─── Panel 8: Three enforcement problems ──────────────────────────────────────
function Panel8() {
  const problems = [
    { x: 86, color: "#6366f1", label: "R1", name: "Confinement", sub: "oriented composites", carrier: "complex ternary", icon: "▲▽" },
    { x: 260, color: "#0ea5e9", label: "R2", name: "Irreversibility", sub: "intrinsic arrow of time", carrier: "pseudoreal binary", icon: "→≁←" },
    { x: 434, color: "#f59e0b", label: "R3", name: "Distinguishability", sub: "tie-breaking label", carrier: "abelian grading", icon: "#" },
  ];
  return (
    <svg viewBox="0 0 520 300" style={{width:"100%",height:"100%"}}>
      <ArrowDef/>
      <text x={260} y={22} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        three independent enforcement problems · each demands its own carrier
      </text>
      {problems.map(p => (
        <g key={p.label}>
          <rect x={p.x-76} y={36} width={152} height={180} rx={6}
            fill={C.panel} stroke={p.color} strokeWidth={1.5} opacity={0.95}/>
          <text x={p.x} y={62} textAnchor="middle" fill={p.color}
            fontSize={22} fontFamily="monospace" fontWeight="700">{p.label}</text>
          <text x={p.x} y={84} textAnchor="middle" fill={C.white}
            fontSize={12} fontFamily="monospace">{p.name}</text>
          <line x1={p.x-60} y1={92} x2={p.x+60} y2={92} stroke={p.color} strokeWidth={0.6} opacity={0.4}/>
          <text x={p.x} y={110} textAnchor="middle" fill={C.faint}
            fontSize={9} fontFamily="monospace">{p.sub}</text>
          <text x={p.x} y={142} textAnchor="middle" fill={p.color}
            fontSize={20} fontFamily="monospace">{p.icon}</text>
          <rect x={p.x-58} y={158} width={116} height={44} rx={3}
            fill={C.bg} stroke={p.color} strokeWidth={0.8} opacity={0.7}/>
          <text x={p.x} y={175} textAnchor="middle" fill={C.text}
            fontSize={9} fontFamily="monospace">carrier:</text>
          <text x={p.x} y={191} textAnchor="middle" fill={p.color}
            fontSize={9} fontFamily="monospace">{p.carrier}</text>
        </g>
      ))}
      <text x={260} y={252} textAnchor="middle" fill={C.text} fontSize={10} fontFamily="monospace">
        three problems · three independent carriers · no overlap
      </text>
      <text x={260} y={268} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        each is required by a separate enforcement gap · not by assumption
      </text>
    </svg>
  );
}

// ─── Panel 9: The gauge group is forced ───────────────────────────────────────
function Panel9() {
  const rows = [
    { family: "Aₙ = SU(n+1)", type: "Complex",    r1: "✓  rank n+1 ≥ 3", color: "#4ec994" },
    { family: "Bₙ = SO(2n+1)", type: "Real",      r1: "✗  no complex carrier", color: "#e05555" },
    { family: "Cₙ = Sp(2n)",   type: "Pseudoreal", r1: "✗  B = B̄",         color: "#e05555" },
    { family: "Dₙ = SO(2n)",   type: "Real",       r1: "✗  no complex carrier", color: "#e05555" },
    { family: "G₂, F₄, E₈",   type: "Real",       r1: "✗",                  color: "#e05555" },
    { family: "E₇",            type: "Pseudoreal", r1: "✗",                  color: "#e05555" },
    { family: "E₆",            type: "Complex",    r1: "✗  min dim=27",      color: "#e05555" },
  ];
  return (
    <svg viewBox="0 0 520 300" style={{width:"100%",height:"100%"}}>
      <ArrowDef/>
      <text x={260} y={18} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        all 17 compact simple Lie algebras · R1 filter (complex ternary carrier)
      </text>
      {rows.map((r,i) => (
        <g key={i}>
          <rect x={20} y={28+i*30} width={480} height={26} rx={3}
            fill={r.color === "#4ec994" ? "rgba(78,201,148,0.08)" : "rgba(224,85,85,0.05)"}
            stroke={r.color} strokeWidth={0.6} opacity={0.8}/>
          <text x={36} y={46+i*30} fill={C.text} fontSize={10} fontFamily="monospace">{r.family}</text>
          <text x={210} y={46+i*30} fill={C.faint} fontSize={9} fontFamily="monospace">{r.type}</text>
          <text x={310} y={46+i*30} fill={r.color} fontSize={10} fontFamily="monospace">{r.r1}</text>
        </g>
      ))}
      <rect x={20} y={244} width={480} height={46} rx={4}
        fill={C.panel} stroke="#4ec994" strokeWidth={1.5}/>
      <text x={260} y={262} textAnchor="middle" fill="#4ec994" fontSize={11} fontFamily="monospace">
        A_n passes · minimality k=N_c=3 selects SU(3)
      </text>
      <text x={260} y={280} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        R2 → SU(2) unique · R3 → U(1) unique · product: SU(3)×SU(2)×U(1)
      </text>
    </svg>
  );
}

// ─── Panel 10: 61 structural channels ─────────────────────────────────────────
function Panel10() {
  const blocks = [
    { label: "45 fermion\ntype-identities", sub: "5 multiplets × 3 gen", count: 45, color: "#0ea5e9", w: 220 },
    { label: "12 gauge\ngenerators",        sub: "8g + 3W + 1B",         count: 12, color: "#6366f1", w: 118 },
    { label: "4 Higgs\ncomponents",         sub: "real scalars",          count: 4,  color: "#f59e0b", w: 54  },
  ];
  let x = 20;
  return (
    <svg viewBox="0 0 520 300" style={{width:"100%",height:"100%"}}>
      <ArrowDef/>
      <text x={260} y={20} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        structural enforcement channels · not kinematic DOF · not helicities
      </text>
      {blocks.map((b,i) => {
        const bx = x;
        x += b.w + 8;
        return (
          <g key={i}>
            <rect x={bx} y={36} width={b.w} height={88} rx={4}
              fill={`${b.color}18`} stroke={b.color} strokeWidth={1.5}/>
            <text x={bx+b.w/2} y={62} textAnchor="middle" fill={b.color}
              fontSize={28} fontFamily="monospace" fontWeight="800">{b.count}</text>
            {b.label.split("\n").map((ln,j) => (
              <text key={j} x={bx+b.w/2} y={88+j*13} textAnchor="middle"
                fill={C.text} fontSize={10} fontFamily="monospace">{ln}</text>
            ))}
            <text x={bx+b.w/2} y={118} textAnchor="middle"
              fill={C.faint} fontSize={8} fontFamily="monospace">{b.sub}</text>
          </g>
        );
      })}
      <text x={260} y={160} textAnchor="middle" fill={C.white}
        fontSize={18} fontFamily="monospace" fontWeight="700">
        45 + 12 + 4 = 61
      </text>
      <rect x={60} y={178} width={400} height={92} rx={4}
        fill={C.panel} stroke={C.border} strokeWidth={1}/>
      <text x={260} y={198} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        L_species: each irreducible representation = one enforcement channel
      </text>
      <text x={260} y={216} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        kinematic DOF (helicity, polarization) are free given the structural commitment
      </text>
      <text x={260} y={236} textAnchor="middle" fill={C.text} fontSize={10} fontFamily="monospace">
        C_total = 61 is a rigid theorem · no free parameters
      </text>
      <text x={260} y={254} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        at Bekenstein saturation each channel costs exactly ε*
      </text>
    </svg>
  );
}

// ─── Panel 11: MECE partition 42 + 3 + 16 ────────────────────────────────────
function Panel11() {
  return (
    <svg viewBox="0 0 520 300" style={{width:"100%",height:"100%"}}>
      <ArrowDef/>
      <text x={260} y={18} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        two binary predicates · mutually exclusive · collectively exhaustive
      </text>
      {/* Q1/Q2 axis labels */}
      <text x={260} y={38} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        Q1: gauge-addressable by external probe?   Q2: conserved non-abelian charge?
      </text>

      {/* Vacuum 42 */}
      <rect x={20} y={54} width={170} height={130} rx={5}
        fill="rgba(99,102,241,0.1)" stroke="#6366f1" strokeWidth={1.5}/>
      <text x={105} y={78} textAnchor="middle" fill="#6366f1"
        fontSize={32} fontFamily="monospace" fontWeight="800">42</text>
      <text x={105} y={98} textAnchor="middle" fill={C.white}
        fontSize={11} fontFamily="monospace">vacuum sector</text>
      <text x={105} y={113} textAnchor="middle" fill={C.faint}
        fontSize={8} fontFamily="monospace">Q1 = 0</text>
      <line x1={36} y1={122} x2={174} y2={122} stroke="#6366f1" strokeWidth={0.5} opacity={0.4}/>
      {["12 gauge generators","27 fermion internal","3 Higgs (Goldstone)"].map((t,i)=>(
        <text key={i} x={105} y={136+i*13} textAnchor="middle"
          fill={C.faint} fontSize={8} fontFamily="monospace">{t}</text>
      ))}

      {/* Baryonic 3 */}
      <rect x={202} y={54} width={116} height={130} rx={5}
        fill="rgba(245,158,11,0.1)" stroke="#f59e0b" strokeWidth={1.5}/>
      <text x={260} y={78} textAnchor="middle" fill="#f59e0b"
        fontSize={32} fontFamily="monospace" fontWeight="800">3</text>
      <text x={260} y={98} textAnchor="middle" fill={C.white}
        fontSize={11} fontFamily="monospace">baryonic</text>
      <text x={260} y={113} textAnchor="middle" fill={C.faint}
        fontSize={8} fontFamily="monospace">Q1=1 · Q2=1</text>
      <line x1={218} y1={122} x2={302} y2={122} stroke="#f59e0b" strokeWidth={0.5} opacity={0.4}/>
      <text x={260} y={138} textAnchor="middle" fill={C.faint}
        fontSize={8} fontFamily="monospace">3 colour charges</text>
      <text x={260} y={151} textAnchor="middle" fill={C.faint}
        fontSize={8} fontFamily="monospace">confined quarks</text>

      {/* Dark 16 */}
      <rect x={330} y={54} width={168} height={130} rx={5}
        fill="rgba(14,165,233,0.1)" stroke="#0ea5e9" strokeWidth={1.5}/>
      <text x={414} y={78} textAnchor="middle" fill="#0ea5e9"
        fontSize={32} fontFamily="monospace" fontWeight="800">16</text>
      <text x={414} y={98} textAnchor="middle" fill={C.white}
        fontSize={11} fontFamily="monospace">dark sector</text>
      <text x={414} y={113} textAnchor="middle" fill={C.faint}
        fontSize={8} fontFamily="monospace">Q1=1 · Q2=0</text>
      <line x1={346} y1={122} x2={482} y2={122} stroke="#0ea5e9" strokeWidth={0.5} opacity={0.4}/>
      {["15 multiplet type-ids","1 physical Higgs"].map((t,i)=>(
        <text key={i} x={414} y={136+i*13} textAnchor="middle"
          fill={C.faint} fontSize={8} fontFamily="monospace">{t}</text>
      ))}

      {/* Total */}
      <rect x={20} y={198} width={478} height={44} rx={4}
        fill={C.panel} stroke={C.border} strokeWidth={1}/>
      <text x={260} y={216} textAnchor="middle" fill={C.white}
        fontSize={13} fontFamily="monospace" fontWeight="700">
        42 + 3 + 16 = 61  ✓
      </text>
      <text x={260} y={232} textAnchor="middle" fill={C.faint}
        fontSize={8} fontFamily="monospace">
        proved saturation-independent (L_sat_part) · result holds at all scales
      </text>

      <text x={260} y={272} textAnchor="middle" fill={C.faint}
        fontSize={8} fontFamily="monospace">
        matter = baryonic + dark = 3 + 16 = 19 · f_b = 3/19 ≈ 16%
      </text>
    </svg>
  );
}

// ─── Panel 12: Capacity fractions → cosmology ─────────────────────────────────
function Panel12() {
  return (
    <svg viewBox="0 0 520 300" style={{width:"100%",height:"100%"}}>
      <ArrowDef/>
      <text x={260} y={18} textAnchor="middle" fill={C.faint} fontSize={9} fontFamily="monospace">
        horizon equipartition (L_equip) · microcanonical argument · one physical input
      </text>

      {/* Logic chain */}
      {[
        { y: 44,  text: "at the causal horizon: entropy maximised (L_irr)", color: C.faint },
        { y: 60,  text: "no preferred ordering among the 61 capacity types", color: C.faint },
        { y: 76,  text: "maximum entropy on N equally-labelled types → equal shares", color: C.faint },
        { y: 92,  text: "Ω_sector = |sector| / C_total", color: C.white },
      ].map((r,i) => (
        <text key={i} x={260} y={r.y} textAnchor="middle"
          fill={r.color} fontSize={10} fontFamily="monospace">{r.text}</text>
      ))}

      {/* Big result boxes */}
      <rect x={30} y={108} width={206} height={90} rx={6}
        fill="rgba(99,102,241,0.12)" stroke="#6366f1" strokeWidth={2}/>
      <text x={133} y={135} textAnchor="middle" fill="#6366f1"
        fontSize={9} fontFamily="monospace">Ω_Λ = 42 / 61</text>
      <text x={133} y={160} textAnchor="middle" fill="#6366f1"
        fontSize={28} fontFamily="monospace" fontWeight="800">0.689</text>
      <text x={133} y={188} textAnchor="middle" fill={C.faint}
        fontSize={8} fontFamily="monospace">observed: 0.690 ± 0.006</text>

      <rect x={284} y={108} width={206} height={90} rx={6}
        fill="rgba(14,165,233,0.1)" stroke="#0ea5e9" strokeWidth={2}/>
      <text x={387} y={135} textAnchor="middle" fill="#0ea5e9"
        fontSize={9} fontFamily="monospace">Ω_m = 19 / 61</text>
      <text x={387} y={160} textAnchor="middle" fill="#0ea5e9"
        fontSize={28} fontFamily="monospace" fontWeight="800">0.311</text>
      <text x={387} y={188} textAnchor="middle" fill={C.faint}
        fontSize={8} fontFamily="monospace">observed: 0.310 ± 0.006</text>

      {/* Footer */}
      <rect x={20} y={216} width={478} height={66} rx={4}
        fill={C.panel} stroke={C.border} strokeWidth={1}/>
      <text x={260} y={234} textAnchor="middle" fill={C.white}
        fontSize={10} fontFamily="monospace">zero free parameters · zero empirical inputs</text>
      <text x={260} y={250} textAnchor="middle" fill={C.faint}
        fontSize={9} fontFamily="monospace">
        the same axiom (A1) that forces non-closure → gauge group → 61 channels
      </text>
      <text x={260} y={266} textAnchor="middle" fill={C.faint}
        fontSize={9} fontFamily="monospace">
        also determines the energy budget of the observable universe
      </text>
    </svg>
  );
}

// ─── Panel data ───────────────────────────────────────────────────────────────
const PANELS = [
  {
    n: 1,
    title: "The hydrogen atom",
    quote: "Consider a hydrogen atom. Two physical distinctions are being maintained at the same interface. The first is the electron's spin: up or down — one binary channel, exactly two states. The second is the electron's position within the orbital: where in the probability cloud is the electron actually found? Position is not binary — it is a continuous stack of binary distinctions, each one asking a finer yes/no question about location. Both draw enforcement capacity from the same local pool.",
    component: Panel1,
  },
  {
    n: 2,
    title: "One shared pool",
    quote: "The interface does not have separate, dedicated infrastructure for spin and separate infrastructure for position — it has a single pool of enforcement channels through which all local distinctions must be routed.",
    component: Panel2,
  },
  {
    n: 3,
    title: "Spin commits — the landscape changes",
    quote: "When the interface commits channels to enforcing the spin distinction, it partitions the local enforcement resources into two camps. The channels that remain for enforcing the position distinction are no longer the same channels that would have been available if spin had not been enforced first.",
    component: Panel3,
  },
  {
    n: 4,
    title: "The interference surplus Δ > 0",
    quote: "The result is that the second task is harder — not because capacity has been 'used up' in a simple bookkeeping sense, but because the first commitment has rearranged the infrastructure. The additional cost is the interference surplus, Δ > 0. It is not an overhead fee or a penalty — it is the genuine cost of enforcing a distinction in a context that has already been shaped.",
    component: Panel4,
  },
  {
    n: 5,
    title: "Path dependence: order matters",
    quote: "Channel rearrangement is not symmetric. The total cost of enforcing spin-then-position is not the same as the total cost of enforcing position-then-spin, because the two orderings produce different rearrangements. This is the operational content of noncommutativity: AB ≠ BA.",
    component: Panel5,
  },
  {
    n: 6,
    title: "Non-closure: A fits, B fits, A+B overflows",
    quote: "Capacity is finite (A1). The interference costs accumulate. Not every combination of individually affordable enforcement tasks remains affordable when composed. Two things that each fit within the budget can collectively exceed it — not because something went wrong, but because the interference surplus pushes the total past the limit.",
    component: Panel6,
  },
  {
    n: 7,
    title: "Why the universe cannot be abelian",
    quote: "The precise non-abelian criterion is order-asymmetric superadditivity: Δ₁₂ ≠ Δ₂₁. A classical congestion system can have Δ > 0 with Δ₁₂ = Δ₂₁ — symmetric contention cost. Only when Δ₁₂ ≠ Δ₂₁ does the algebra become genuinely non-commutative. This asymmetry is derived from Schur's lemma on the irreducible Hilbert space forced by A1 — it has no classical analogue. Order-asymmetric superadditivity, not mere superadditivity, forces non-abelian gauge structure.",
    component: Panel7,
  },
  {
    n: 8,
    title: "Three enforcement problems",
    quote: "Non-abelian structure arrives in three independent flavours, each solving a different enforcement problem. Confinement: oriented composites must be distinguishable from their anti-composites — requires a complex ternary carrier (R1). Irreversibility: the gauge sector must contain intrinsically irreversible processes in isolation, not merely inherit entropy from the environment — requires a pseudoreal binary carrier (R2). Distinguishability: when two states share the same non-abelian labels, a third carrier resolves the tie — requires an abelian grading (R3).",
    component: Panel8,
  },
  {
    n: 9,
    title: "The gauge group is forced",
    quote: "Exhaustive classification of all 17 compact simple Lie algebras eliminates every family but one. Complex carrier → A_n = SU(N_c) family passes; all others excluded. Pseudoreal 2-dimensional carrier → SU(2) is unique. Abelian grading → U(1) is unique. Capacity minimality selects N_c = 3: the antisymmetric invariant of SU(N_c) has rank k = N_c; minimum k = 3 forces N_c = 3. The gauge group SU(3) × SU(2) × U(1) is the unique surviving product structure.",
    component: Panel9,
  },
  {
    n: 10,
    title: "61 structural enforcement channels",
    quote: "Counting the distinct structural enforcement channels — not field-theoretic degrees of freedom, not kinematic modes, but irreducible representations each contributing exactly one enforcement channel — yields C_total = 61. Fermion type-identities: 45 (five multiplet types × three generations). Gauge generators: 12 (8 gluons + 3 weak + 1 hypercharge). Higgs real components: 4. Every channel costs exactly ε* at Bekenstein saturation.",
    component: Panel10,
  },
  {
    n: 11,
    title: "The MECE partition: 42 + 3 + 16",
    quote: "Two binary predicates partition all 61 channels exhaustively and without overlap. Q1: is the channel gauge-addressable by an external probe? Q2: does it carry a conserved non-abelian charge? The partition is: vacuum sector (Q1=0): 42 channels — gauge generators, Goldstone modes, and fermion internal structure. Baryonic sector (Q1=1, Q2=1): 3 channels — the three confined colour charges. Dark sector (Q1=1, Q2=0): 16 channels — the 15 matter type-identities plus one physical Higgs.",
    component: Panel11,
  },
  {
    n: 12,
    title: "From capacity fractions to cosmology",
    quote: "At the causal horizon, where irreversibility forces entropy to its maximum and no further information arrives, the framework assigns no preferred ordering among the 61 capacity types. Maximum entropy on 61 discrete equally-unlabelled types means each type carries an equal share. The energy density fraction of any sector equals its type-count fraction: Ω_sector = |sector| / 61. This gives Ω_Λ = 42/61 = 0.689 and Ω_m = 19/61 = 0.311 — no free parameters, no empirical inputs.",
    component: Panel12,
  },
];

// ─── Main ─────────────────────────────────────────────────────────────────────
export default function Storyboard() {
  const [current, setCurrent] = useState(0);
  const panel = PANELS[current];
  const PanelComponent = panel.component;

  useEffect(() => {
    const handler = (e) => {
      if (e.key === "ArrowRight" || e.key === "ArrowDown")
        setCurrent(c => Math.min(c + 1, PANELS.length - 1));
      if (e.key === "ArrowLeft" || e.key === "ArrowUp")
        setCurrent(c => Math.max(c - 1, 0));
    };
    window.addEventListener("keydown", handler);
    return () => window.removeEventListener("keydown", handler);
  }, []);

  return (
    <div style={{
      background: C.bg,
      minHeight: "100vh",
      fontFamily: "'Courier New', monospace",
      color: C.text,
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      padding: "16px",
      boxSizing: "border-box",
    }}>
      {/* Header */}
      <div style={{ textAlign: "center", marginBottom: "10px" }}>
        <div style={{ fontSize: "10px", letterSpacing: "0.18em", color: C.faint, marginBottom: "3px" }}>
          PAPER 2 · THE STRUCTURE OF ADMISSIBLE PHYSICS
        </div>
        <div style={{ fontSize: "13px", color: C.faint, letterSpacing: "0.06em" }}>
          from the hydrogen atom to Ω_Λ = 42/61
        </div>
      </div>

      {/* Progress dots */}
      <div style={{ display: "flex", gap: "8px", marginBottom: "14px", alignItems: "center" }}>
        {PANELS.map((p, i) => (
          <button key={i} onClick={() => setCurrent(i)}
            style={{
              width: i === current ? "28px" : "8px",
              height: "8px",
              borderRadius: "4px",
              border: "none",
              cursor: "pointer",
              background: i === current ? C.accent1 : i < current ? C.muted : C.dim,
              transition: "all 0.25s",
              padding: 0,
            }} />
        ))}
        <span style={{ color: C.faint, fontSize: "10px", marginLeft: "4px" }}>
          {current + 1} / {PANELS.length}
        </span>
      </div>

      {/* Panel title */}
      <div style={{
        fontSize: "15px", fontWeight: "700", color: C.white,
        marginBottom: "12px", letterSpacing: "0.04em", textAlign: "center",
      }}>
        {panel.n}. {panel.title}
      </div>

      {/* SVG diagram */}
      <div style={{
        width: "100%", maxWidth: "560px",
        background: C.panel,
        border: `1px solid ${C.border}`,
        borderRadius: "6px",
        aspectRatio: "560/300",
        overflow: "hidden",
      }}>
        <PanelComponent />
      </div>

      {/* Quote from paper */}
      <div style={{
        maxWidth: "560px", width: "100%",
        marginTop: "14px",
        padding: "14px 16px",
        background: C.panel,
        border: `1px solid ${C.border}`,
        borderRadius: "6px",
        borderLeft: `3px solid ${C.accent1}`,
        fontSize: "11px",
        lineHeight: "1.85",
        color: C.faint,
        fontStyle: "italic",
      }}>
        "{panel.quote}"
      </div>

      {/* Navigation */}
      <div style={{ display: "flex", gap: "12px", marginTop: "14px", alignItems: "center" }}>
        <button onClick={() => setCurrent(c => Math.max(c - 1, 0))}
          disabled={current === 0}
          style={{
            padding: "8px 22px", fontSize: "11px", letterSpacing: "0.1em",
            border: `1px solid ${current === 0 ? C.dim : C.border}`,
            borderRadius: "2px", cursor: current === 0 ? "default" : "pointer",
            background: C.panel,
            color: current === 0 ? C.dim : C.text,
          }}>
          ← prev
        </button>

        <span style={{ color: C.faint, fontSize: "10px" }}>← → keys</span>

        <button onClick={() => setCurrent(c => Math.min(c + 1, PANELS.length - 1))}
          disabled={current === PANELS.length - 1}
          style={{
            padding: "8px 22px", fontSize: "11px", letterSpacing: "0.1em",
            border: `1px solid ${current === PANELS.length - 1 ? C.dim : C.accent1}`,
            borderRadius: "2px",
            cursor: current === PANELS.length - 1 ? "default" : "pointer",
            background: current === PANELS.length - 1 ? C.panel : "#0f2040",
            color: current === PANELS.length - 1 ? C.dim : C.accent1,
          }}>
          next →
        </button>
      </div>

      {/* Footer */}
      <div style={{ marginTop: "16px", color: C.dim, fontSize: "9px", textAlign: "center" }}>
        APF · E. S. Brooke 2026 · ← → to navigate
      </div>
    </div>
  );
}
