# AEGIS AI Historical Data Specification

**Version:** 1.0

------------------------------------------------------------------------

## Purpose

This document defines the canonical historical market data format used
throughout AEGIS AI.

Every historical data source---whether exported from MetaTrader 5,
TradingView, Binance, Interactive Brokers, or another provider---must be
converted into this format before entering the AEGIS application.

The objective is to provide one consistent representation of historical
market data so that the remainder of the system remains completely
independent of external providers.

------------------------------------------------------------------------

# Design Principles

The historical data format must be:

-   Provider independent
-   Human readable
-   Easy to validate
-   Easy to generate
-   Easy to replay
-   Compatible with future adapters
-   Compatible with paper trading
-   Compatible with backtesting

------------------------------------------------------------------------

# File Format

Historical data shall be stored as UTF-8 encoded CSV files.

The first row must contain the column headers.

Example:

``` csv
timestamp,open,high,low,close,tick_volume
2026-07-01T09:00:00Z,3300.00,3303.00,3299.00,3302.00,1000
2026-07-01T09:05:00Z,3302.00,3305.00,3301.00,3304.00,1015
```

------------------------------------------------------------------------

# Required Columns

  Column        Type           Description
  ------------- -------------- ------------------
  timestamp     ISO-8601 UTC   Candle open time
  open          Decimal        Opening price
  high          Decimal        Highest price
  low           Decimal        Lowest price
  close         Decimal        Closing price
  tick_volume   Integer        Tick volume

All required columns must be present.

------------------------------------------------------------------------

# Optional Columns

  Column        Type      Description
  ------------- --------- --------------------------
  real_volume   Integer   Exchange reported volume
  spread        Integer   Broker spread

If omitted, these values shall become `None` within the domain model.

------------------------------------------------------------------------

# Timestamp

AEGIS stores every timestamp internally as UTC.

Preferred format:

``` text
2026-07-01T09:00:00Z
```

Timezone-aware ISO-8601 timestamps may also be accepted, but they will
always be converted to UTC before entering the domain.

------------------------------------------------------------------------

# Numeric Types

Price fields shall be parsed as `Decimal`.

-   open
-   high
-   low
-   close

Volume fields shall be parsed as integers.

-   tick_volume
-   real_volume
-   spread

------------------------------------------------------------------------

# Ordering

Rows must be ordered chronologically.

Oldest candle first.

Newest candle last.

The HistoricalMarketAdapter may reject data that is not in chronological
order.

------------------------------------------------------------------------

# Missing Data

The following fields are mandatory:

-   timestamp
-   open
-   high
-   low
-   close
-   tick_volume

Rows containing missing mandatory values should be rejected.

------------------------------------------------------------------------

# Instrument

Each CSV file represents one instrument.

The instrument is supplied by the caller rather than stored inside the
CSV.

Example:

``` python
adapter.get_candles(
    instrument=gold,
    timeframe=Timeframe.M5,
    count=500,
)
```

------------------------------------------------------------------------

# Timeframe

Each CSV file represents one timeframe.

The timeframe is supplied by the caller rather than stored inside the
CSV.

------------------------------------------------------------------------

# HistoricalMarketAdapter Responsibilities

The HistoricalMarketAdapter is responsible for:

-   Reading historical data
-   Validating the input format
-   Parsing timestamps
-   Parsing Decimal prices
-   Parsing integer volumes
-   Constructing immutable `Candle` objects
-   Returning a `CandleSeries`

The adapter is **not** responsible for:

-   Technical indicators
-   Market structure detection
-   Trend analysis
-   Trading decisions
-   Risk assessment

Its sole responsibility is translating historical data into AEGIS domain
objects.

------------------------------------------------------------------------

# Canonical Example

``` csv
timestamp,open,high,low,close,tick_volume
2026-07-01T09:00:00Z,3300.00,3303.00,3299.00,3302.00,1000
2026-07-01T09:05:00Z,3302.00,3305.00,3301.00,3304.00,1015
2026-07-01T09:10:00Z,3304.00,3308.00,3303.00,3307.00,1040
```

------------------------------------------------------------------------

# Future Compatibility

Future providers should convert their native formats into this
specification before entering the application layer.

Examples include:

-   MetaTrader 5
-   TradingView exports
-   Binance
-   Interactive Brokers
-   Polygon.io
-   Twelve Data
-   Yahoo Finance
-   Database-backed historical stores

By standardizing on this format, the application layer, perception
layer, reasoning layer, replay engine, paper trading engine, and future
live trading components remain completely independent of the original
data source.

------------------------------------------------------------------------

# Summary

This specification defines the canonical historical market data contract
for AEGIS AI.

Every historical adapter shall produce a `CandleSeries` from data
conforming to this specification, ensuring one consistent,
provider-independent pathway into the AEGIS domain model.
