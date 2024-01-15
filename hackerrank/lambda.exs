defmodule Reader do
  def read(type \\ :string) do
    case type do
      :str -> read_line()
      :int -> read_line() |> String.to_integer()
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
  def polygon(data) do
    first =
      data
      |> Enum.map(fn element ->
        element
        |> String.split(" ")
        |> Enum.map(&String.to_integer/1)
      end)

    last = tl(first) ++ [hd(first)]

    f(first, last, [])
    |> Enum.reduce(0, fn i, acc ->
      [[x, y], [a, b]] = i
      acc + distance(x, y, a, b)
    end)
    |> IO.inspect()
  end

  def f([], [], r), do: r

  def f([h1 | t1], [h2 | t2], r) do
    f(t1, t2, r ++ [[h1, h2]])
  end

  def distance(x, y, a, b) do
    (:math.pow(x - a, 2) + :math.pow(y - b, 2))
    |> :math.sqrt()
  end
end

n = Reader.read(:int)

for _ <- 1..n do
  Reader.read(:str)
end
|> Solution.polygon()
