from core import Atom, Molecule

def read_molecule(r):
    '''(reader) -> Molecule
    
    Read a single molecule from r and return it,
    or return None to signal end of file.
    '''
    # If there isn't another line, we're at the end of the file.
    line = r.readline()
    if not line:
        return None
    
    # Name of the molecule: "COMPND name"
    key, name = line.split()
    # Other lines are "END" or "ATOM num kind x y z"
    molecule = Molecule(name)
    reading = True
    while reading:
        line = r.readline()
        if line.startswith('END'):
            reading = False
        else:
            key, num, kind, x, y, z = line.split()
            molecule.add(Atom(num, kind, float(x), float(y), float(z)))
    return molecule

def main():
    with open('ammonia.pdb') as f:
        molecules = []
        mol = read_molecule(f)
        while mol:
            molecules.append(mol)
            mol = read_molecule(f)
    
    for m in molecules:
        print(m)

if __name__ == '__main__':
    main()