# Milionaire Game

## Zadania wstępne:

1. Pytania po uruchomieniu gry powinny być wyświetlane losowo
2. Dlaczego metoda `get_next_question()` w klasie Game jest nieoptymalna i co mozemy zrobić zeby to zmienić?

## OOP podstawy

### Enkapsulacja 

Dodaj prywatną metodę, która będzie formatować pytanie oraz dla klasy `Game` prywatne atrybuty, które będą przechowywać indeks bieżącego pytania i wynik, ograniczając bezpośredni dostęp do tych danych z zewnątrz klasy

`_format_question_and_options` w `Question` to prywatna metoda, która formatuje pytanie i opcje odpowiedzi, używana tylko przez metodę __str__, co ukrywa jej implementację przed użytkownikami klasy.
`_current_question_index` i `_score` w `Game` to prywatne atrybuty, które są używane do śledzenia stanu gry i wyników, chroniąc te dane przed nieautoryzowanym dostępem i modyfikacją z zewnątrz klasy.


### Dziedziczenie 

Dodaj klasę `TimedGame`, która dziedziczy wszystko po `Game` i dodaje teorytyczne ograniczenie czasowe.

- Dziedziczenie, polimorfizm i przysłanianie metod 

Dodaj klasę `HintGame` i `TimedGame`, które dziedziczą po klasie Game

`TimedGame` dodaje logikę związaną z ograniczeniem czasowym i karą czasową za błędne odpowiedzi.
`HintGame` wprowadza możliwość uzyskania podpowiedzi dotyczącej odpowiedzi.

```python

class TimedGame(Game):
    def __init__(self, questions, time_limit):
        pass

    def submit_answer(self, answer):
        # Specjalna logika dla gry z czasem
        # Przy poprawnej odpowiedzi wyświetla Remaining time
        # Przy błędnej odpowiedzi odejmuje czas jako karę i wyświetla Remaining time
        pass

class HintGame(Game):
    def __init__(self, questions, hints_allowed):
        pass

    def request_hint(self, current_question):
        # Sprawdzaczy uztkownik ma prawo do podpowiedzi
        # Jeśli tak uzytkownik otrzymuje podpowiedz np. "Hint: The answer starts with letter: {first letter}"
        # W przeciwnym wypadku wyświetl komunikat informujacy ze uzytkownik wykorzytal wszystkie podpowiedzi
        pass
```


Gdyby dodać menu wyboru, w którym uzytkownik moze wybrac rodzaj gry (basic, hinted, timed) mozna by rowniez dodać polimorfizm

## OOP zagadnienia zaawansowane


### Dunder Methods 

Utwórz dla `TimedGame` i `HintGame` specyficzne dla nich metody specjalne `__str__`

Dodatkowo do klasy `Game` dodaj `__getitem__` i `__setitem__` jako metody, które można użyć do bezpośredniego dostępu do pytań w grze, traktując obiekt gry jak kontener.
__len__ - metoda może zwracać liczbę pytań w grze.

```python
class Game:
     def __len__(self):
        pass

    def __getitem__(self, ...):
        pass

    def __setitem__(self, ...):
       pass

    # Przykład użycia
    # game[0] zwróci pierwsze pytanie
    # game[0] = new_question ustawi nowe pytanie na pierwszej pozycji, gdzie new_question jest obiektem typu Question

```


### Definicja funkcji pomocniczych jako first-class objects

Możemy zdefiniować funkcje pomocnicze do sprawdzania odpowiedzi lub aktualizacji wyniku, które następnie mogą być przekazywane do klas gry czyli spełniają warunenk
Zdefiniuj funkcję `check_answer_correct()` zwracającą wartości `True`/`False`.

Następnie wprowadź wykorzystanie funkcji `check_answer_correct()` jako domyślnej funkcji sprawdzającej odpowiedzi. Dodaj jej wykorzystanie do konstruktora klasy `Game`. 

**Funkcja poza klasą Game:**

```python
def check_answer_correct(question, answer):
    return question.correct_answer == answer
```

### Definiowanie funkcji wyższego rzędu

Dodaj atrybut difficulty do klasy Question, który umożliwi filtrowanie pytań na podstawie poziomu trudności.
Dodaj funkcję wyższego rzędu, która zwraca funkcję filtrującą pytania na podstawie poziomu trudności.
Dodaj funcję wyszego rzędu, która która modyfikuje wyniki za poprawną odpowiedź na pytanie tak by podwoić punkty.

Kroki:

**Poziom trudności**

1. Dodaj atrybut difficulty do konstruktora klasy Question.
2. Zmodyfikuj konstruktor, aby przyjmował nowy parametr difficulty i przypisywał go do atrybutu instancji.
3. Zaktualizuj wszelkie instancje klasy Question w kodzie, dodając odpowiedni poziom trudności do każdej z nich.


**Tworzenie funkcji wyższego rzędu do filtrowania pytań**

1. Zdefiniuj funkcję wyższego rzędu `difficulty_filter`, która przyjmuje parametr level (poziom trudności) i zwraca inną funkcję filtrującą pytania na podstawie tego poziomu.
2. Stwórz funkcję wewnętrzną, która będzie przyjmować pojedyncze pytanie jako argument i zwracać True lub False w zależności od tego, czy pytanie spełnia kryterium poziomu trudności.

**Modyfikacja systemu punktacji za pomocą funkcji wyższego rzędu**

1. Napisz funkcję wyższego rzędu `score_modifier`, która przyjmuje wartość punktów bazowych i zwraca inną funkcję, która oblicza końcową liczbę punktów na podstawie tego, czy odpowiedź była poprawna.
2. Stwórz funkcję wewnętrzną, która przyjmuje argument określający, czy odpowiedź była poprawna, i mnoży wartość bazową razy dwa dla poprawnych odpowiedzi.
3. Zaktualizuj konstruktor klasy `Game` by umoliwość rozszerzenie o nową kalkulację punktacji.


## Rozszerzenie

Dodaj w funkcjach pomocniczych odczyt pytań z pliku do odpowiednich instancji klasy `Question`.

* Przykładowy format jako plik JSON

```json
[
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "correct_answer": "Paris",
        "difficulty": "easy"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "2", "5"],
        "correct_answer": "4",
        "difficulty": "easy"
    },
    {
        "question": "Who wrote 'Macbeth'?",
        "options": ["Shakespeare", "Austen", "Joyce", "Hemingway"],
        "correct_answer": "Shakespeare",
        "difficulty": "medium"
    }
]

```