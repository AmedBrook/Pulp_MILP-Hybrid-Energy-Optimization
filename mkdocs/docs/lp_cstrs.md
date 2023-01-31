#### Linear programming constraints.

Linear programming constraints (LP constraints) are the rules that gouverne the problem optimization process. They are fondamentally set of equations, they might be either inequality equations ( exmaple : ${a} + {b} \le {c}\hspace{0.3cm}$)   or equality equations  ( exmaple : ${a} + {b} = {c}\hspace{0.3cm}$) constructed based on the LP variables quantities and problem parameters. (See. Problem LP variables and Problem LP constraints). 

#### Set of problem LP constraints.



- Load requirements:     $\hspace{1cm}L_k =P_k^{\mathrm{load}} +\eta {\;}^{\mathrm{fromBat}} {\cdot \;P}_k^{\mathrm{fromBat}}\hspace{3.6cm}$      $k=1,\dots ,n$  


- Power split:   $\hspace{2cm}P_{k\;} =P_k^{\mathrm{load}} {+\;P}_k^{\mathrm{toBat}}\hspace{6.3cm}$   $k=1,\dots ,n$

- Charge balance (initial):   $\hspace{1cm}Q_0 =Q_{\mathrm{init}}\hspace{6.3cm}$  

- Charge balance:  $\hspace{0.5cm}Q_k =Q_{k-1} +\eta^{\mathrm{toBat}} \cdot \;P_k^{\mathrm{toBat}} \Delta t-\;P_k^{\mathrm{fromBat}} \Delta t\hspace{1.8cm}$     $k=1,\dots ,n$ 


- Charge balance (final):     $\hspace{1cm}Q_n =Q_{\mathrm{final}}\hspace{3cm}$   


- Logical conditions on genset: $\hspace{1cm}P_{k\;} \le {0\ldotp 9P}_{\mathrm{max}\;} {\cdot y}_k\hspace{4.7cm}$    $k=1,\dots ,n$ 


- (0 or in 0.2P_max - 0.9Pmax):  $\hspace{1cm}P_{k\;} \le {0\ldotp 2P}_{\mathrm{max}\;} {\cdot y}_k\hspace{4.5cm}$    $k=1,\dots ,n$




- Logical conditions on battery:   $\hspace{1.9cm}y_k^{\mathrm{toBat}} +y_{k\;}^{\mathrm{fromBat}} \le 1\hspace{3.4cm}$     $k=1,\dots ,n$  
$\newline$     
$\hspace{6.9cm}P_k^{\mathrm{toBat}} \le 0\ldotp 9P_{\mathrm{max}} {\cdot y}_k^{\mathrm{toBat}}\hspace{3cm}$ $k=1,\dots ,n$ 


$\hspace{6.9cm}P_k^{\mathrm{fromBat}} \le 0\ldotp 9P_{\mathrm{max}} {\cdot \;y}_k^{\mathrm{fromBat}}\hspace{2.4cm}$  $k=1,\dots ,n$ 

