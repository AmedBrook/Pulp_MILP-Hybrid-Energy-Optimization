Problem LP variables
====================

#### Linear programming variables.

Linear programing variables (Lp varaibles for short), are the decision variables that will host the calculation optimzation process values for each physical quantities used along this problem. Those LP variable are used later on to fotmulate the problem constraints (See. LP constraints). 



#### Set of linear programming variables.


$Q_{\mathrm{bat}} \hspace{1cm}$ : Maximal energy charge stored in battery (kWh).

$P_{\mathrm{From_bat}} \hspace{0.5cm}$ : Maximal energy charge stored in battery (kWh).

$P_{\mathrm{A}} \hspace{1.3cm}$ : Maximal energy charge stored in battery (kWh).

$P_{\mathrm{A_load}} \hspace{1cm}$ : Maximal energy charge stored in battery (kWh).

$Z \hspace{1.6cm}$ : Maximal energy charge stored in battery (kWh).

$FC_{\mathrm{A}} \hspace{1cm}$ : Maximal energy charge stored in battery (kWh).

$P_{\mathrm{Ato_bat}} \hspace{0.8cm}$ : Maximal energy charge stored in battery (kWh).

$Y_{\mathrm{to_bat}} \hspace{1cm}$ : Maximal energy charge stored in battery (kWh).

$Y_{\mathrm{from_bat}} \hspace{0.7cm}$ : Maximal energy charge stored in battery (kWh).

$Y \hspace{1.6cm}$ : Maximal energy charge stored in battery (kWh).


#### Variables' lower and upper bounds.

- $\hspace{1cm}0\ldotp 2.Q_{\mathrm{max}} \le Q_k \le Q_{\mathrm{max}}\hspace{5.5cm}$ $k=0,\ldotp \ldotp \ldotp ,n$ 
- $\hspace{1cm}0\le P_k \le 0\ldotp 9.P_{\mathrm{max}}\hspace{6.5cm}$  $k=1,\ldotp \ldotp \ldotp ,n$    
 
- $\hspace{1cm}0\le P_k^{\mathrm{to_Bat}} ,P_k^{\mathrm{from_Bat}} \le {0\ldotp 9.P}_{\mathrm{max}}\hspace{4cm}$ $k=1,\ldotp \ldotp \ldotp ,n$ 


- $\hspace{1cm}0\le z_k \le 1\hspace{8.1cm}$  $k=2,\ldotp \ldotp \ldotp ,n$

#### Variables' types.

- Continuous : $\hspace{2cm}Q_k,P_k^{\mathrm{to_Bat}} ,P_k^{\mathrm{from_Bat}} ,z_k$ 

- Semi-continuous : $\hspace{1cm}P_k$ 

- Binary : $\hspace{3cm}y_k ,\hspace{1.5cm}y_k^{\mathrm{to_Bat}} ,\hspace{1.5cm}y_k^{\mathrm{from_Bat}}$