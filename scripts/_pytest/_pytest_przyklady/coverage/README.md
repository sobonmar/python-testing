# Coverage Testing Guide

## Przygotowanie
```bash
# Instalacja pakietu pytest-cov
pip install pytest-cov
```

## Kod do testowania
- `calculator.py` - prosty kalkulator z różnymi funkcjami
- `test_calculator.py` - niepełne testy (demonstracja coverage)

## Sposoby mierzenia coverage

### 1. Coverage z pytest-cov (najpopularniejsze)

#### Console output
```bash
pytest --cov=calculator
pytest --cov=calculator --cov-report=term-missing
```

#### HTML report (najwygodniejszy)
```bash
pytest --cov=calculator --cov-report=html
# Otwórz htmlcov/index.html w przeglądarce
```

#### XML report (dla CI/CD)
```bash
pytest --cov=calculator --cov-report=xml
# Tworzy coverage.xml
```

### 2. Bezpośrednio z coverage.py

#### Uruchomienie testów
```bash
coverage run -m pytest
```

#### Console report
```bash
coverage report
coverage report -m  # z brakującymi liniami
```

#### HTML report
```bash
coverage html
# Otwórz htmlcov/index.html
```

#### XML report
```bash
coverage xml
```

#### JSON report
```bash
coverage json
```

### 3. Zaawansowane opcje

#### Wykluczenie plików z coverage
```bash
pytest --cov=. --cov-report=html --ignore=tests/
```

#### Minimalny próg coverage (test fails jeśli < 80%)
```bash
pytest --cov=calculator --cov-fail-under=80
```

#### Coverage z konkretną konfiguracją
```bash
# Utwórz .coveragerc
pytest --cov=calculator --cov-config=.coveragerc
```

### 4. Konfiguracja w pytest.ini
```ini
[tool:pytest]
addopts = 
    --cov=calculator
    --cov-report=term-missing
    --cov-report=html:htmlcov
    --cov-branch
    --cov-fail-under=80
```

### 5. Konfiguracja w .coveragerc
```ini
[run]
source = calculator
omit = 
    */tests/*
    */venv/*
    setup.py

[report]
exclude_lines =
    pragma: no cover
    def __repr__
    raise AssertionError
    raise NotImplementedError
```

## Interpretacja wyników

- **Line coverage**: % pokrytych linii kodu
- **Branch coverage**: % pokrytych ścieżek w if/else
- **Missing lines**: które linie nie są testowane

## Dobre praktyki

1. **80% coverage to dobry cel** (nie 100%)
2. **HTML report najlepszy do analizy** - pokazuje dokładnie co nie jest testowane
3. **Branch coverage lepsze niż line coverage** - wykrywa więcej problemów
4. **Ignoruj nieistotne linie** (np. `pass`, `raise NotImplementedError`)
5. **Coverage to narzędzie, nie cel** - ważna jest jakość testów, nie liczba

## Ćwiczenie - Popraw Coverage

Aktualnie coverage jest około 60-70%. Żeby osiągnąć >90%, musisz dodać 5 brakujących testów:

1. **Test divide by zero error**
2. **Test is_positive with positive number**
3. **Test is_positive with negative number**
4. **Test get_grade negative score error**
5. **Test get_grade F**

Po dodaniu tych testów coverage powinien wzrosnąć do >90%.