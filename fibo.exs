defmodule Reader do
  def read(type \\ :string) do
    case type do
      :str -> read_line()
      :int -> read_line() |> String.to_integer()
      :float -> read_line() |> Float.parse()
    end
  end

  defp read_line() do
    IO.read(:stdio, :line) |> String.replace("\n", "")
  end
end

defmodule Solution do
  def find(nth) do
    list = [1, 1]

    ([0] ++ fib(list, nth))
    |> Enum.at(nth - 1)
  end

  def fib(list, 2) do
    Enum.reverse(list)
  end

  def fib(list, n) do
    [first_elem, second_elem | _] = list
    fib([first_elem + second_elem | list], n - 1)
  end
end

Reader.read(:int)
|> Solution.find()
|> IO.puts()
