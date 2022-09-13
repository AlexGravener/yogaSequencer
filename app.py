import random
from poseClass import pose

#Pose library
#Pose class comprises (id, name, intensity, primary, secondary, is_wu, is_yin, is_vin, is_power, is_cd)
cobra = pose("cobra", "Cobra", 2, ["back"], ["shoulders"], True, False, True, False, False)
seal = pose("seal", "Seal", 3, ["back"], ["shoulders"], True, False, True, False, False)
upDog = pose("upDog", "Up dog", 4, ["arms"], ["back"], False, False, True, True, False)

downDog = pose("downDog", "Down dog", 2, ["arms"], ["back"], True, False, True, True, False)
dolphin = pose("dolphin", "Dolphin", 4, ["arms"], ["shoulders"], False, False, True, True, False)

child = pose("child", "Child's pose", 1, ["back"], ["shoulders"], True, True, False, False, True)
extChild = pose("extChild", "Extended child's pose", 1, ["back"], ["hips"], True, True, False, False, True)
hero = pose("hero", "Hero's pose", 1, ["legs"], ["feet"], True, True, False, False, True)
heroToes = pose("heroToes", "Hero's pose with toes tucked under", 2, ["feets"], ["legs"], True, True, False, False, False)

staff = pose("staff", "Staff pose", 2, ["legs"], ["back"], True, True, False, False, True)
headKnee = pose("headKnee", "Head to knee pose", 2, ["back"], ["legs"], True, True, False, False, True)

mountain = pose("mountain", "Mountain pose", 1, ["whole body"], ["none"], True, False, True, True, True)
volcano = pose("volcano", "Volcano pose", 2, ["arms"], ["whole body"], False, False, True, True, False)
tree = pose("tree", "Tree pose", 3, ["legs", "hips"], ["core", "balance"], False, False, True, True, False)

warrior1_R = pose("warrior1_R", "Warrior one on the right", 3, ["legs"], ["arms"], False, False, True, True, False)
warrior1_L = pose("warrior1_L", "Warrior one on the left", 3, ["legs"], ["arms"], False, False, True, True, False)
warrior2_R = pose("warrior2_R", "Warrior two on the right", 3, ["legs"], ["arms"], False, False, True, True, False)
warrior2_L = pose("warrior2_L", "Warrior two on the left", 3, ["legs"], ["arms"], False, False, True, True, False)
warrior3_R = pose("warrior3_R", "Warrior three on the right", 4, ["legs"], ["core", "balance"], False, False, True, True, False)
warrior3_L = pose("warrior3_L", "Warrior three on the left", 4, ["legs"], ["core", "balance"], False, False, True, True, False)

lowLunge_R = pose("lowLunge_R", "Low lunge on the right", 2, ["hips"], ["legs", "arms"], True, False, True, True, False)
lowLunge_L = pose("lowLunge_L", "Low lunge on the left", 2, ["hips"], ["legs", "arms"], True, False, True, True, False)
lizardLunge_R = pose("lizardLunge_R", "Lizard lunge on the right", 2, ["hips"], ["legs", "arms"], False, False, True, True, False)
lizardLunge_L = pose("lizardLunge_L", "Lizard lunge on the left", 2, ["hips"], ["legs", "arms"], False, False, True, True, False)
highLunge_R = pose("highLunge_R", "High lunge on the right", 3, ["legs"], ["arms"], False, False, True, True, False)
highLunge_L = pose("highLunge_L", "High lunge on the light", 3, ["legs"], ["arms"], False, False, True, True, False)
sideLunge_R = pose("sideLunge_R", "Side lunge on the right", 2, ["legs"], ["ankles", "feet"], False, False, True, True, False)
sideLunge_L = pose("sideLunge_L", "Side lunge on the left", 2, ["legs"], ["ankles", "feet"], False, False, True, True, False)

yogi = pose("yogi", "Yogi squat", 3, ["hips"], ["ankles, feet"], True, True, True, True, True)
frog = pose("frog", "Froggy squat", 2, ["hips"], ["ankles", "feet"], True, True, False, False, False)
chair = pose("chair", "Chair pose", 3, ["core", "legs"], ["balance"], False, False, True, True, False)
standPigeon_R = pose("standPigeon_R", "Standing pigeon on the right", 4, ["legs"], ["core", "balance"], False, False, False, True, False)
standPigeon_L = pose("standPigeon_L", "Standing pigeon on the left", 4, ["legs"], ["core", "balance"], False, False, False, True, False)

example = pose("example", "Example", 3, ["arms", "chest"], ["legs"], False, True, True, False, True)

poses = [cobra, seal, upDog, downDog, child, extChild, hero, heroToes, staff, headKnee, mountain, volcano, tree,
         warrior1_R, warrior1_L, warrior2_R, warrior2_L, warrior3_R, warrior3_L, lowLunge_R, lowLunge_L, lizardLunge_R,
         lizardLunge_L, highLunge_R, highLunge_L, sideLunge_R, sideLunge_L, yogi, frog, chair, standPigeon_R, standPigeon_L, example]


#Sequence parameters
styleInput = input("What style of yoga would you like to practise?\n")
style = styleInput[0:3].lower()
primaries = ["legs", "arms", "back", "shoulders", "hips"]
duration = 600
warmUp = duration * 0.2
mainFlow = duration * 0.6
coolDown = duration * 0.2

#function initial values
sequence = []
identities = []
potential = random.choice(poses)
length = 0

#functions

def addPose(primaries, potential, length):
    for i in potential.primary:
        if i in primaries:
            if not sequence:
                sequence.append(potential.name)
                identities.append(potential.id)
                length += 50
                return length
            else:
                last = sequence[-1]
                if potential.name != last:
                    sequence.append(potential.name)
                    identities.append(potential.id)
                    length += 50
                    return length
                else:
                    return length
        else:
            return length

def checkSymmetry(sequence, length):
    if not sequence:
        pass
    else:
        last = identities[-1]
        if "_R" in last:
            for count, ele in enumerate(poses):
                if last == ele.id:
                    other = count + 1
                    equalise = poses[other]
                    sequence.append(equalise.name)
                    identities.append(equalise.id)
                    length += 50
                    return length
        elif "_L" in last:
            for count, ele in enumerate(poses):
                if last == ele.id:
                    other = count - 1
                    equalise = poses[other]
                    sequence.append(equalise.name)
                    identities.append(equalise.id)
                    length += 50
                    return length
    return length

def pickWarmUp(primaries):
    length = 0
    while length < warmUp:
        potential = random.choice(poses)
        if potential.is_wu:
            length = addPose(primaries, potential, length)
            length = checkSymmetry(sequence, length)

def pickYin(primaries):
    length = 0
    while length < mainFlow:
        potential = random.choice(poses)
        if potential.is_yin:
            length = addPose(primaries, potential, length)
            length = checkSymmetry(sequence, length)

def pickVin(primaries):
    length = 0
    while length < mainFlow:
        potential = random.choice(poses)
        if potential.is_vin:
            length = addPose(primaries, potential, length)
            length = checkSymmetry(sequence, length)

def pickPow(primaries):
    length = 0
    while length < mainFlow:
        potential = random.choice(poses)
        if potential.is_pow:
            length = addPose(primaries, potential, length)
            length = checkSymmetry(sequence, length)

def pickCoolDown(primaries):
    length = 0
    while length < coolDown:
        potential = random.choice(poses)
        if potential.is_cd:
            length = addPose(primaries, potential, length)
            length = checkSymmetry(sequence, length)

if style == "yin":
    print("This is a yin practice, let's start with a warm up")
    pickWarmUp(primaries)
    print(sequence)
    sequence = []
    identities = []
    print("Now for the main flow")
    pickYin(primaries)
    print(sequence)
    sequence = []
    identities = []
    print("And finally let's cool down")
    pickCoolDown(primaries)
    print(sequence)

elif style == "vin":
    print("This is a vinyasa flow, let's start with a warm up")
    pickWarmUp(primaries)
    print(sequence)
    sequence = []
    identities = []
    print("Now for the main flow")
    pickVin(primaries)
    print(sequence)
    sequence = []
    identities = []
    print("And finally let's cool down")
    pickCoolDown(primaries)
    print(sequence)

elif style == "pow":
    print("This is a power yoga flow, let's start with a warm up")
    pickWarmUp(primaries)
    print(sequence)
    sequence = []
    identities = []
    print("Now for the main flow")
    pickPow(primaries)
    print(sequence)
    sequence = []
    identities = []
    print("And finally let's cool down")
    pickCoolDown(primaries)
    print(sequence)

