#!/usr/bin/env python3


class DeterministicFiniteAutomata:
    """Processor for deterministic finite automata machines"""

    def __init__(
        self,
        states: set,
        alphabet: set,
        transitions: set,
        startState: str,
        accepting: set,
    ) -> None:
        self.__states = states
        self.__alphabet = alphabet
        self.__transitions = dict()
        self.__accepting = set()
        self.__start = startState

        # Generate Accepting States
        for a in accepting:
            if a in self.__states:
                self.__accepting.add(a)
            else:
                raise ValueError(f"State {a} not found in set of declared states.")

        # Generate Transitions
        for t in transitions:
            if self.__transitions.get(t[0]) is None:
                self.__transitions[t[0]] = dict()
            if t[0] in self.__states and t[2] in self.__states:
                self.__transitions[t[0]][t[1]] = t[2]
            else:
                transitionStateDifference = {t[0], t[2]}.difference(self.__states)
                raise ValueError(
                    f"States {transitionStateDifference} not found in set of declared states."
                )

    def process_input(self, expression: str):
        """Start process of determining acceptance or non-acceptance of expression"""

        alphabetExpressionDifference = set(expression).difference(self.__alphabet)
        if len(alphabetExpressionDifference) > 0:
            raise ValueError(
                f"Attempted to process symbols {alphabetExpressionDifference} not found in alphabet."
            )
        return self.__perform_process(expression)

    def __perform_process(self, expression: str, currentState: str = ""):
        """Recursively process expressions, checking whether they are accepted or rejected by the machine"""

        length = len(expression)
        if currentState == "":
            currentState = self.__start
        if length == 0 and currentState in self.__accepting:
            return True
        elif length == 0 and currentState not in self.__accepting:
            return False
        else:
            return self.__perform_process(
                expression[1::], self.__transitions[currentState][expression[0]]
            )

    @staticmethod
    def parse_machine_string(machine: str):
        """Return a machine based on the machine string given"""
        machine
        raise NotImplementedError


def main():
    """Run the program"""
    print("Running program...")

    # Machine which only accepts if three consecutive 0's are found in a row somewhere in the string
    DFA = DeterministicFiniteAutomata(
        {"q1", "q2", "q3", "q4"},
        {"0", "1"},
        {
            ("q1", "0", "q2"),
            ("q1", "1", "q1"),
            ("q2", "0", "q3"),
            ("q2", "1", "q1"),
            ("q3", "0", "q4"),
            ("q3", "1", "q1"),
            ("q4", "0", "q4"),
            ("q4", "1", "q4"),
        },
        "q1",
        {"q4"},
    )
    print(DFA.process_input("01000"))
    print(DFA)


if __name__ == "__main__":
    main()
