defmodule Reader do
  def read(type \\ :string) do
    case type do
      :str -> read_line()
      :int -> read_line() |> String.to_integer()
      :float -> read_line() |> Float.parse()
      :eof -> read_eof([])
    end
  end

  defp read_line() do
    IO.read(:stdio, :line) |> String.replace("\n", "")
  end

  defp read_eof(prev) do
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
  def solve(list) do
    f = fn x -> if x, do: "YES", else: "NO" end

    list
    |> Enum.map(fn [a, b] -> b / a end)
    |> Enum.reduce([true, -1], fn x, [v, i] ->
      cond do
        i == -1 -> [v, x]
        v == false -> [false, x]
        true -> [i == x, x]
      end
    end)
    |> Kernel.hd()
    |> f.()
  end
end

n = Reader.read(:int)

for _ <- 1..n do
  line = Reader.read(:int)

  1..line
  |> Enum.map(fn _ ->
    Reader.read(:str)
    |> String.split()
    |> Enum.map(&String.to_integer/1)
  end)
  |> Solution.solve()
  |> IO.puts()
end
