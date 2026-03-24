Transaction Analysis Engine

This project simulates a transaction processing system.

The user inputs values until typing "finish". Each value represents:
- positive: income
- negative: expense
- 0: invalid transaction

System Structure

Storage
Original values are stored without modification.

Classification
Each value becomes:
[value, type]

Normalization
A new structure is created:
[original_value, type, processed_value]

Processed values are always positive and multiplied by 2.

Analysis
The system calculates:
- average
- maximum
- minimum
- total income 
- total expenses
- count of each type

 Purpose

This project trains:
- list handling
- data structures
- separation of concerns
- logical thinking

 Execution

Run the file and enter values.
Type "finish" to stop input.