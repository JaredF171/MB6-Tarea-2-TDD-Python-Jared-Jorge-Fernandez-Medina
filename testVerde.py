from mayor import mayor

try:
    def probar_tests_mayor():
        assert mayor([3, 9, 2]) == 9
        assert mayor([]) is None

    probar_tests_mayor()
    print("Todos los tests PASARON (verde) ✅")
except Exception as e:
    import traceback
    traceback.print_exc()