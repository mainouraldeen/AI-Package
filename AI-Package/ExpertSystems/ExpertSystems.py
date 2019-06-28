from pyknow import *

########################################################################################################################
# Q1
class Doctor(KnowledgeEngine):

    ###
    @Rule(Fact(age=P(lambda x: x <= 5)))
    def child(self):
        self.declare(Fact(patient='child'))
        print("child")

    ###
    @Rule(Fact(age=P(lambda x: x > 5)))
    def adult(self):
        self.declare(Fact(patient='adult'))
        print("adult")

    ###
    # done
    @Rule(AND(Fact(patient='child'),
              Fact(symptoms=P(lambda sym: sym.__len__() > 2 and set(sym) <= set(
                  ["shakiness", "hunger", "sweating", "headache", "pale"])))))
    def func1(self):
        self.declare(Fact(disease='low sugar'))
        print("low sugar")

    ####
    # done
    @Rule(AND(Fact(patient='child'),
              Fact(symptoms=P(lambda sym: sym.__len__() > 2 and set(sym) <= set(
                  ["thirst", "blurred vision", "headache", "dry mouth", "smelling breath", "shortness of breath"])))))
    def func2(self):
        self.declare(Fact(disease='high sugar'))
        print("high sugar")

    ###
    # done
    @Rule(Fact(disease="low sugar"), Fact(parents="y"))
    def func3(self):
        self.declare(Fact(disease="diabetic"))
        print("Diabetic")

    ###
    # done
    @Rule(Fact(nose="runny"), Fact(cough="harsh"))
    def fun4(self):
        self.declare(Fact(disease="cold"))
        print("cold")

    ###
    # done
    @Rule(Fact(disease="cold"), Fact(patient="child"),
          AND(Fact(symptoms={"brownish-pink rash", "high temperature",
                             "fast temperature", "bloodshot eyes", "white spots inside cheek"})))
    def func5(self):
        self.declare(Fact(disease="measles"))
        print("measles")

    ###
    # done
    @Rule(AND(Fact(patient='child'), Fact(temperature="moderate"),
              Fact(saliva="not normal"), Fact(mouth="dry"),
              Fact(neck_lymph_nodes="swollen")))
    def func6(self):
        self.declare(Fact(disease="mumps"))
        print("mumps")

    ###
    # done
    @Rule(Fact(patient='child'), (Fact(disease="cold")),
          Fact(symptoms={"weakness", "strong body aches", "vomiting", "sore throat", "sneezing"}))
    def func7(self):
        self.declare(Fact(disease='child-flu'))
        print("child-flu")

    ###
    # done
    @Rule(Fact(patient='adult'), (Fact(disease="cold")),
          Fact(symptoms={"weakness", "strong body aches", "vomiting", "sore throat", "sneezing"}))
    def func8(self):
        self.declare(Fact(disease='adult-flu'))
        print("adult-flu")


########################################################################################################################
# Q2
class plant(Fact):
    pass


class tuber(Fact):
    pass


class plantDiagnoses(KnowledgeEngine):
    @DefFacts()
    def plantFacts(self):
        yield plant(temp="low", humidity="high")
        yield plant(temp="high", humidity="normal")
        yield plant(temp="normal", humidity="normal")

        yield tuber(colour="reddish-brown", skin="spots")
        yield tuber(colour="brown", skin="wrinkles")
        yield tuber(state="normal", skin="spots")
        yield tuber(state="dry", skin="circles")

    @Rule(AND(plant(temp="high", humidity="normal"), tuber(colour="reddish-brown", skin="spots")))
    def black_heart(self):
        print("the plant has black heart.")

    @Rule(AND(plant(temp="low", humidity="high"), tuber(state="normal", skin="spots")))
    def late_blight(self):
        print("the plant has late blight.")

    @Rule(AND(plant(temp="high", humidity="normal"), tuber(state="dry", skin="circles")))
    def dry_rot(self):
        print("the plant has dry rot.")

    @Rule(AND(plant(temp="normal", humidity="normal"), tuber(colour="brown", skin="wrinkles")))
    def early_blight(self):
        print("the plant has early blight.")


########################################################################################################################
# Q1 *Testcase*
def main():
    medical = Doctor()
    medical.reset()
    print("########################Q1 Medical ExpertSyestem########################")
    # Q1
    medical.declare(Fact(age=3), Fact(symptoms=["shakiness", "hunger"]))

    # Q2
    medical.declare(Fact(patient='child'), Fact(symptoms=["dry mouth", "blurred vision", "headache"]))

    # Q3
    medical.declare(Fact(disease="low sugar"), Fact(parents="y"))

    # Q4
    medical.declare(Fact(nose="runny"), Fact(cough="harsh"))

    # Q5
    medical.declare(Fact(patient="child"), Fact(
        symptoms={"bloodshot eyes", "brownish-pink rash", "high temperature", "fast temperature",
                  "white spots inside cheek"}))

    # Q6
    medical.declare(Fact(age=4), Fact(temperature="moderate"),
                    Fact(saliva="not normal"), Fact(mouth="dry"),
                    Fact(neck_lymph_nodes="swollen"))

    # Q7
    medical.declare(Fact(patient='child'), (Fact(disease="cold")),
                    Fact(symptoms={"weakness", "strong body aches", "vomiting", "sore throat", "sneezing"}))

    # Q8
    medical.declare(Fact(age=13), (Fact(disease="cold")),
                    Fact(symptoms={"weakness", "strong body aches", "vomiting", "sore throat", "sneezing"}))

    medical.run()
    ########################################################################################################################
    print("####################Q2 plantDiagnoses ExpertSyestem####################")
    # q2 main
    engine = plantDiagnoses()
    engine.reset()
    engine.run()


# end main fn
########################################################################################################################




# main fn call
main()
