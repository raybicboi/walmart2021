# walmart2021

The program can be run by using a CLI of choice, cd into the directory and run "python walmart.py"

Note that there is a filereader that reads in 'test.txt', so the txt file must be in the same directory for the program to run. The program will generate 'out.txt' that contains
the results of the deliverable.

# Assumptions

The main assumption is that when possible, new entrants choose to sit in the middle of the theater (by row) as opposed to the front or the back. We can extend the assumption 
to say new entrants would prefer to sit in the middle of the row rather than the side, but the tradeoff is that finals week is coming up so I feel like the scope I provided is
fine.

Logistically, a party of 21+ people will not be allowed because the core logic checks by row if there are enough remaining seats. I can extend this by separating a large party
using the mod operator. For example, a party of 42 can be split into three parties of 20, 20, and 2.

At some point, the final row will be filled with buffers of three seats. At this point if more tickets are bought, they can STILL be seated as long as they are at most a
party of three. In this case, they would occupy the seats of the buffers, starting with the middle rows again.

Members of the same party will always get adjacent seats- and if there aren't enough, the entire party will be placed to the next row. If the following party is small and can fit
in the previous row, then they will be placed there. For example, if there are 4 seats remaining in row 4 (buffer seats aside), the next party of 5+ will be placed in row 5.
However, if the following party only has two, then they will be placed in the remaining seats of row 4. This is assuming row 4 is checked before row 5. Otherwise, there is no
optimization algorithm happening- technically we can maximize the number of entrants by making sure a party of 4 fills out that row instead of a party of 2 and wasting two seats
as the buffer, but I did not check for those cases.

The test file needs to be identical to that in the spec sheet and contain no extra characters or whitespace. I provided a 'test.txt' with the program that covers some edge cases.

Lastly, I have not tested this, but I am unsure if the file reader works for four+ digit ticket numbers. All of the ticket values in the test file follows RXXX, where 'X' is
a digit between 0 and 9.
