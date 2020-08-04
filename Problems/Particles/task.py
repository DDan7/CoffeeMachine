spin = input()
elec_charge = input()

if spin == "1/2":
    if elec_charge == "-1/3":
        print("Strange Quark")
    elif elec_charge == "2/3":
        print("Charm Quark")
    elif elec_charge == "-1":
        print("Electron Lepton")
    elif elec_charge == "0":
        print("Muon Lepton")
elif spin == "1":
    if elec_charge == "0":
        print("Photon Boson")
elif spin == "0":
    if elec_charge == "0":
        print("Higgs boson Boson")
