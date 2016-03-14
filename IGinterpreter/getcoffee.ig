Program(
  Cons(
    Vertex(
      1,
      DoUntil(
        Move(5, 0, 0, 0.5, 0.5),
        Stop(0.1, "landmark[1]"),
        Next(2)
      )
    ),
    Cons(
      Vertex(
        2,
        DoUntil(
          Move(0, 0, -12.5, 0.2, 0.2),
          Stop(0.1, "landmark[2]"),
          Next(3)
        )
      ),
      Cons(
        Vertex(
          3,
          Do(
            Move(5, 0, 0, 0.5, 0.5),
            Next(4)
          )
        ),
        Cons(
          Vertex(
            4,
            Do(
              Move(0, 0, -1.57, 0.2, 0.2),
              Next(5)
            )
          ),
          Cons(
            Vertex(
              5,
              Conditional(
                Visible("landmark[3]"),
                Next(6),
                Next(7)
              )
            ),
            Cons(
              Vertex(
                6,
                Do(
                  Say("Can I get a coffee please?"),
                  End
                )
              ),
              Singleton(
                Vertex(
                  7,
                  Do(
                    Move(0, 0, 0, 0, 0),
                    End
                  )
                )
              )
            )
          )
        )
      )
    )
  ),
  Start(1)
)
