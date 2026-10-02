# Task 0: AI SQL to ORM Refactoring and Security Analysis

## Overview
This task demonstrates refactoring a procedural database script that uses raw SQL into an object-oriented, type-safe implementation using SQLAlchemy ORM.

## Files
- `initial_procedural.py`: Original legacy procedural code using MySQL connector.
- `orm_refactored.py`: Refactored code utilizing SQLAlchemy ORM declarative models and session handling.
- `README.md`: Task documentation.

## Key Technical & Security Highlights
1. **SQL Injection Mitigation**: Parameters are safely bound by SQLAlchemy ORM engines, eliminating direct string execution risks.
2. **Session Unit-of-Work**: Database operations are atomic and safely managed with context-managed sessions.
3. **Database Dialect Independence**: Switching database engines requires updating only the connection URL string.
