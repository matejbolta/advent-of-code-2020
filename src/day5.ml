# load "str.cma";; (* windows *)

let day = "5"

let pass_to_rowcol p = (String.sub p 0 7, String.sub p 7 3)

let binary_to_decimal_pair (row, col) =
  let bin_to_dec bin = (* string -> int *)
    let bin = Str.split (Str.regexp "") bin in
    let rec aux i acc = function
      | [] -> acc
      | x :: xs when x = "1" ->
        aux (i - 1) (acc + int_of_float (2. ** float_of_int i)) xs
      | _ :: xs -> aux (i - 1) acc xs
    in
    aux (List.length bin - 1) 0 bin
  in
  (row
  |> Str.global_replace (Str.regexp "F") "0"
  |> Str.global_replace (Str.regexp "B") "1"
  |> bin_to_dec,
  col
  |> Str.global_replace (Str.regexp "L") "0"
  |> Str.global_replace (Str.regexp "R") "1"
  |> bin_to_dec)
;;

let pair_to_passid (row, col) = 8 * row + col

let rec list_to_max m = function [] -> m | x :: xs -> list_to_max (max m x) xs

let rec find_id = function
  | [] | _ :: [] -> failwith "No such id"
  | x :: y :: tail -> if y - x <> 1 then x + 1 else find_id (y :: tail)
;;

let naloga1 vsebina =
  let s = vsebina
    |> String.trim
    |> String.split_on_char '\n'
    |> List.map pass_to_rowcol
    |> List.map binary_to_decimal_pair
    |> List.map pair_to_passid
    |> list_to_max 0
    |> string_of_int
  in
  print_endline ("day " ^ day ^ ", puzzle 1: " ^ s);
  s
;;

let naloga2 vsebina =
  let s = vsebina
    |> String.trim
    |> String.split_on_char '\n'
    |> List.map pass_to_rowcol
    |> List.map binary_to_decimal_pair
    |> List.map pair_to_passid
    |> List.fast_sort
      (fun x y -> if x > y then 1 else if x < y then -1 else 0)
    |> find_id
    |> string_of_int
  in
  print_endline ("day " ^ day ^ ", puzzle 2: " ^ s);
  s
;;

let _ =
  let preberi_datoteko ime_datoteke =
    let chan = open_in ime_datoteke in
    let vsebina = really_input_string chan (in_channel_length chan) in
    close_in chan;
    vsebina
  and izpisi_datoteko ime_datoteke vsebina =
    let chan = open_out ime_datoteke in
    output_string chan vsebina;
    close_out chan
  in

  let vsebina_datoteke = preberi_datoteko ("data/day_" ^ day ^ ".in") in
  let odgovor1 = naloga1 vsebina_datoteke
  and odgovor2 = naloga2 vsebina_datoteke
  in

  izpisi_datoteko ("out/day_" ^ day ^ "_1.out") odgovor1;
  izpisi_datoteko ("out/day_" ^ day ^ "_2.out") odgovor2
;;