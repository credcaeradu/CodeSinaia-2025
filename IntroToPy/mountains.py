from dataclasses import dataclass

@dataclass
class munte:
    nume: str
    alt: int
    tara: str
    iso: str

m: munte

def functie (file_name):
    print("in fuction")
    with open (file_name,"r",encoding = "utf-8") as f:
        for line in f.readlines():
            m=input()
    print (m)

if __name__ == "__main__":
    print("here")
    functie("IntroToPy/mountains2_db.tsv")