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
  def absolute(list) do
    list
    |> Enum.map(&String.to_integer/1)
    |> Enum.map(&abs(&1))
    |> Enum.each(&IO.puts(&1))
  end
end

list = Reader.read(:eof)
Solution.absolute(list)
