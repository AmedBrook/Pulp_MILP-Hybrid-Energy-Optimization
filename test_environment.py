
import sys
REQUIRED_PYTHON = "python" 

def main():
    
############## Testing the required python version  ##############################

    system_major = sys.version_info.major
    if REQUIRED_PYTHON == "python":
        required_major = 2
    elif REQUIRED_PYTHON == "python3":
        required_major = 3
    else:
        raise ValueError("Unrecognized python interpreter: {}".format(
            REQUIRED_PYTHON))

    if system_major != required_major:
        raise TypeError(
            "This project requires Python {}. Found: Python {}".format(
                required_major, sys.version))
    else:
        print(">>> The required Python version passes all tests!")

############ Testing the required Pulp version ##########################################

    import pulp
    pulp_version = pulp. VERSION
    if pulp_version != "2.7.0":
        raise TypeError(
            "This project requires Pulp version 2.7.0" )
    else:
        print(">>> Pulp version passes test!")
    
############ Testing installed pulp packages ###############################################

    import pulp
    if pulp.pulpTestAll() != 'OK' : 
        pulp.pulpTestAll()
    else: 
        print('Pupl has been successsfully tested')



    if __name__ == '__main__':
        main()