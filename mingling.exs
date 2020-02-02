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

Reader.read(:str)
|> String.graphemes()
|> Enum.uniq()
|> Enum.join()
|> IO.puts()
