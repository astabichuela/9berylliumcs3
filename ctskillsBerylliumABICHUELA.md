# Annex A
## Computational Thinking Exercise: 
### "Smart School Canteen Queue

**Section: 9 - Beryllium**
**Score:**____________

**Name:** Armel Sean T. Abichuela
**Date:** August 19, 2026


Scenario

The PSHS school canteen is small and often gets crowded during lunch break. Students line up to buy food, but the process is slow because:

- Some students take too long to decide what to order.
- The cashier has to manually calculate totals and give change.
- There is no system to track which food items are running out.

Your group’s task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills.


Step 1: Identify the Big Problem

Main Problem:
The canteen’s current system cannot handle the high demand efficiently, resulting in long waiting times and overcrowding.



Step 2: Identify three to four Sub-Problems
Please list possible sub-problems:  

1. Slow ordering decisions of Students.

2. Cashiers using manual transactions.

3. Overcrowding of the small canteen.



Step 3: Define Computational Thinking Approaches
For each sub-problem, apply CT skills:

Sub-Problem
1. Slow ordering decisions of Students.
2. Cashiers using manual transactions.
3. Overcrowding of the small canteen.

CT Skill
1. Abstraction
2. Algorithm
3. Decomposition

Example Solution
1. A board that tells the student the prices and recommendations for what to order
2. A cashier system similar to what the CO-OP uses now and if applicable upgrade it to touch screen to reduce error and speed up the transaction.
3. Make the schedule of Lunch breaks differ for each grade levels or make the schedules for grades 7-9 is 11am-12am, and grades 10-12 is 12nn-1pm



Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem

### START
 ### DISPLAY menu with item names and prices
  ### INITIALIZE total = 0
###
 ### WHILE customer has not finished ordering
 ### PROMPT customer to select item
 ### ADD item price to total
 ### ASK if customer wants to order more
 ### END WHILE
###
  ### DISPLAY "Total amount: " + total
  ### PROMPT customer for payment amount
###
  ### IF payment >= total THEN
  ### change = payment - total
  ### DISPLAY "Change: " + change
  ### PRINT receipt with items, total, payment, and change
  ### ELSE
  ### DISPLAY "Insufficient payment. Please try again."
  ### REPEAT payment process
  ### END IF
### END