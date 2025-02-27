def main():
    print("Find your trees age!")
    print()

    tree_dict = {
        "red maple" : 4.5,
        "silver maple" : 3.0,
        "sugar maple" : 5.0,
        "river birch" : 3.5,
        "white birch" : 5.0,
        "shagbark hickory" : 7.5,
        "green ash" : 4.0,
        "black walnut" : 4.5,
        "black cherry" : 5.0,
        "white oak" : 5.0,
        "red oak" : 4.0,
        "pin oak" : 3.0,
        "linden or brassword" : 3.0,
        "american elm" : 4.0,
        "ironwood" : 7.0,
        "cottonwood" : 2.0,
        "dogwood" : 7.0,
        "redbud" : 7.0
    }

    for tree in tree_dict:
        print(f"-{tree}")


    while True:

        u_tree_type = input("Please choose a tree to measure from the list: ").lower()

        growth_factor = tree_dict.get(u_tree_type)
        if growth_factor is not None:
            break
        else:
            print("Invalid tree type. Please try again.\n")
    
    while True:
        u_tree_circ = input("What is the circumference of the tree?: ")

        try:
            u_tree_circ = float(u_tree_circ)
            if u_tree_circ > 0:
                break
            else:
                print("Invalid input. Tree circumference cannot be less than or equal to zero.\n")
        except ValueError:
            print("Invalid input. Circumference must be a number.\n")



    tree_age = float((u_tree_circ / 3.14159) * growth_factor)

    print("The tree is approximately {} years old.".format(round(tree_age), 2))

    input("Press 'Enter' to quit: ")


if __name__ == "__main__":
    main()