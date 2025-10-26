peptides = ["SAFTPAT(1)AT(1)GS(1)S(1)PS(1)PVLGQGEK",
"GSCGIGGGIGGGS(1)S(1)R(1)",
"GSCGIGGGIGGGS(1)S(1)R",
"EQLS(1)T(1)S(1)EENS(1)K(1)K",
"EQLS(1)T(1)S(1)EENS(1)KK",
]

ptm_dict = {"ph":["S","T","Y"],
            "ac":["K"]}



se = "SAFTPAT(1)AT(1)GS(1)S(1)PS(1)PVLGQGEK"

pos = se.findall("(1)")

print(pos)