# Pytest Hooks - Przykłady

## Fixtures vs Hooks

**Fixtures** = dla **konkretnych testów** (opt-in)
- `def test_something(fixture):` - musisz jawnie użyć
- Setup/teardown dla wybranych testów
- Dependency injection

**Hooks** = dla **wszystkich testów** globalnie (automatic)  
- `def pytest_runtest_setup(item):` - działa dla KAŻDEGO testu
- Cross-cutting concerns (logging, raportowanie)
- Rozszerzanie mechanizmów pytest

## Czym są hooki?

**Hooki** to punkty zaczepienia w cyklu życia pytest. Pozwalają "wczepić się" w różne momenty wykonywania testów i dodać własną logikę.

## Popularne hooki pytest

| Hook | Kiedy się wykonuje |
|------|-------------------|
| `pytest_configure` | Na początku sesji |
| `pytest_collection_modifyitems` | Po zebraniu testów |
| `pytest_runtest_setup` | Przed każdym testem |
| `pytest_runtest_call` | Podczas testu |
| `pytest_runtest_teardown` | Po teście |
| `pytest_runtest_logreport` | Przy logowaniu wyniku |
| `pytest_sessionfinish` | Na końcu sesji |

## Zastosowania hooków

- **Logging** - dodatkowe logi przed/po testach
- **Setup/Cleanup** - przygotowanie środowiska
- **Raportowanie** - własne formaty wyników
- **Modyfikacja testów** - dodawanie markerów, filtrowanie
- **Integracje** - wysyłanie wyników do zewnętrznych systemów
- **Debugowanie** - dodatkowe informacje o testach