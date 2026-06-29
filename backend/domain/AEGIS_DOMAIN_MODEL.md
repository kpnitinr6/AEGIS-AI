# AEGIS Domain Model

> "Understand the market before making a decision."

---

# Vision

AEGIS is not a trading bot.

AEGIS is an explainable market intelligence platform.

Its purpose is to observe the market, understand its structure, reason about
institutional behaviour, and only then assist in making trading decisions.

Every domain object represents a real concept that exists in financial markets,
independent of any broker, exchange, trading platform, or strategy.

The domain models facts.

Application services derive knowledge from those facts.

Trading decisions are produced only after sufficient evidence has been collected.

---

# Core Principles

## 1. Market First

The core models the market, not the broker.

Broker-specific concepts belong in adapters.

Examples:

✓ Candle
✓ Price
✓ Swing
✓ Trend
✓ Liquidity

Examples that DO NOT belong in the core:

✗ MT5 Ticket
✗ Magic Number
✗ Broker Symbol
✗ Order Filling Mode
✗ Contract Size
✗ Margin Mode

---

## 2. Facts Before Decisions

AEGIS never jumps directly from data to trades.

Instead:

Market Data
    ↓
Market Reality
    ↓
Market Memory
    ↓
Market Structure
    ↓
Market Context
    ↓
Reasoning
    ↓
Decision

Every layer builds upon the previous one.

---

## 3. Explainability

Every conclusion produced by AEGIS must be explainable.

The system must always be capable of answering:

Why?

Every decision should be traceable back to observable market facts.

---

## 4. Immutable Domain

Domain objects represent facts.

Facts do not change.

Whenever practical, all domain objects should be immutable.

---

## 5. Domain Owns the Language

The domain defines the vocabulary used throughout the application.

Examples:

Price

Swing

Higher High

Break of Structure

Trend

Liquidity

Order Block

Application services consume this language.

They never redefine it.

---

# Domain Layers

## Layer 1 — Market Reality

Represents observable facts.

Instrument

Time

Timeframe

Price

Candle

CandleSeries

---

## Layer 2 — Market Memory

Represents remembered observations.

Swing

SwingType

SwingSequence

---

## Layer 3 — Market Structure

Represents interpreted structure.

StructureType

StructurePoint

MarketStructure

---

## Layer 4 — Market State

Represents the current state of the market.

Trend

TrendState

---

## Layer 5 — Market Context

Provides institutional context.

Support

Resistance

Liquidity

Order Blocks

Fair Value Gaps

Volume Profile

---

## Layer 6 — Reasoning

Produces evidence.

Confidence

Risk

Reward

Bias

Narrative

---

## Layer 7 — Decision

Produces recommendations.

Long

Short

No Trade

---

# Design Rules

Every class should answer:

What real market concept does this represent?

Every service should answer:

How is this concept detected?

Every engine should answer:

Why does this matter?

---

# Long-Term Goal

AEGIS should eventually be capable of explaining its own reasoning in natural language.

Example:

"The market formed a Higher Low after a confirmed Break of Structure on the M15 timeframe. Liquidity above the previous swing high was consumed while the H1 trend remained bullish. The current bias therefore remains long."

The explanation is the product.

The trade is merely a consequence.

# The AEGIS Constitution

1. Model reality before modelling strategies.
2. Prefer domain concepts over indicators.
3. Store facts, derive knowledge.
4. Every conclusion must be explainable.
5. Make invalid states impossible.
6. The domain owns the language.
7. Keep the core independent of brokers, exchanges, and vendors.
8. Favor composition over duplication.
9. One responsibility per class.
10. Quality over speed.
11. Every feature requires automated tests.


# The AEGIS Manifesto

AEGIS exists to understand financial markets before attempting to predict them.

It does not begin with indicators.

It begins with observable reality.

Every conclusion made by AEGIS must be explainable.

Every decision must be supported by evidence.

Every layer of intelligence is built upon verified market facts.

The purpose of AEGIS is not to automate trading.

The purpose of AEGIS is to model market behaviour so accurately that intelligent decisions become a natural consequence.

The explanation is as valuable as the prediction.

If AEGIS cannot explain a conclusion, it should not make one.


# What is AEGIS?

AEGIS is an Explainable Market Intelligence Platform.

It observes markets.

It remembers market events.

It understands market structure.

It reasons about market behaviour.

It explains its conclusions.

Trading is merely one possible application of this intelligence.

# The Five Laws of AEGIS

1. Observe before concluding.

2. Remember before comparing.

3. Understand before predicting.

4. Explain before deciding.

5. Learn continuously without compromising evidence.

# The AEGIS Engineering Oath

When contributing to AEGIS:

I will model reality before strategy.

I will prefer clarity over cleverness.

I will build explainable systems.

I will keep the domain pure.

I will avoid hidden assumptions.

I will write tests before trusting behaviour.

I will remember that market intelligence is the product.

Every line of code should make AEGIS easier to understand, easier to extend, and easier to trust.

