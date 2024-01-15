defmodule Reader do
  def read(type \\ :string) do
    case type do
      :str -> read_line()
      :int -> read_line() |> String.to_integer()
    end
  end

  defp read_line() do
    IO.read(:stdio, :line) |> String.replace("\n", "")
  end
end

defmodule Solution do
  def sum(a, b) do
    a + b
  end
end

a = Reader.read(:int)
b = Reader.read(:int)
c = Solution.sum(a, b)
IO.puts(c)
