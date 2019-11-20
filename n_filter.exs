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
  def filter_positions(list) do
    list
    |> Enum.map(&String.to_integer/1)
    |> Enum.with_index()
    |> Enum.each(fn {x, y} ->
      if rem(y + 1, 2) == 0, do: IO.puts(x)
    end)
  end
end

list = Reader.read(:eof)
Solution.filter_positions(list)
