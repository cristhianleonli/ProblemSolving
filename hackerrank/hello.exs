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
  def print(n, w) do
    1..n
    |> Enum.each(fn _ -> IO.puts(w) end)
  end
end

n = Reader.read(:int)
Solution.print(n, "Hello World")
