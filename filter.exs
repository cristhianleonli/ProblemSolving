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

  def read_eof(prev) do
    case IO.read(:stdio, :line) do
      :eof ->
        prev

      {:error, reason} ->
        IO.puts("Error: #{reason}")

      data ->
        string = data |> String.replace("\n", "")
        read_eof(prev ++ [string])
    end
  end
end

defmodule Solution do
  def filter(n, list) do
    list
    |> Enum.map(&String.to_integer/1)
    |> Enum.filter(fn x -> x < n end)
    |> Enum.each(&IO.puts(&1))
  end
end

n = Reader.read(:int)
data = Reader.read_eof([])
Solution.filter(n, data)
