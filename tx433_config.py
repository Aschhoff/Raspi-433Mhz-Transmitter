
# Config Datei fuer tx433_pi.py


tx_pin=18           # PI GPIO Pin 18 als TX

# devicename {protokoll,addresse 1-4095 ,unit 1-n} quigg7000
# devicename {protokoll,addresse 1-1000000 ,state 1-15} ev1527

devices={"Schalter1":{"prot":"tx_quigg7000","addr":"2816","unit":"2","state":"1"},
         "Schalter2":{"prot":"tx_quigg7000","addr":"2816","unit":"2","state":"0"},
         "Klingel":{"prot":"tx_ev1527","addr":"535723","state":"1"},
         "Fenster":{"prot":"tx_ev1527","addr":"30164","state":"1"},
         "Bimmel":{"prot":"pt8a978","code":"40","tx_pin":tx_pin},
         "rawdata":{"sync":"14000","short":"400","long":"1400","code":"111011001000011111111100"}
        
       }
















