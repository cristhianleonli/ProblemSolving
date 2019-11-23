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
  def replicate(n, list) do
    list
    |> Enum.each(&Solution.print(&1, n))
  end

  def print(x, n) do
    1..n
    |> Enum.each(fn _ -> IO.puts(x) end)
  end
end

n = Reader.read(:int)
data = Reader.read(:eof)
Solution.replicate(n, data)
