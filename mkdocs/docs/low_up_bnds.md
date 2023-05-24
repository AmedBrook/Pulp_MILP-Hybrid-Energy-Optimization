## Variables bounds.
---
Linear programing variables are the variables whose values the optimizer will solve for in each time step, those variables are bounded from both sides (lower and upper) to finite the problem region of values and hence lowering the complexity to solve it.

![Screenshot](img/hyh_illustration_lpvariables.png)

#### Upper and lower bounds
---
| LPvariable                    | Lower bound                                      | Upper bound
| ------------------------      | --------------                                   | --------
| $Q_k^{\mathrm{bat}}$          | $0\ldotp 2.Q_{\mathrm{max}}$                     | $Q_{\mathrm{max}}$
| $P_{k}$                       | $P_{\mathrm{min}}$                               | $0.9.P_{\mathrm{max}}$
| $P_k^{\mathrm{load}}$         | $P_{\mathrm{min}}$                               | $0.9.P_{\mathrm{max}}$
| $P_k^{\mathrm{to\_bat}}$      | $P_{\mathrm{min}}$                               | $0.9.P_{\mathrm{max}}$
| $P_k^{\mathrm{from\_bat}}$    | $P_{\mathrm{min}}$                               | $0.9.P_{\mathrm{max}}$
| $Y_k$                         | 0                                                | 1
| $Y_k^{\mathrm{to\_bat}}$      | 0                                                | 1
| $Y_k^{\mathrm{from\_bat}}$    | 0                                                | 1
| $Z$                           | 0                                                | 1
| $FOC$                         | 0                                                | $FOC_{max}$