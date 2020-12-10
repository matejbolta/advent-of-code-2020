let day = "9"


let get_previous_25 index input_list =
  let rec aux_25 acc i =
    if List.length acc = 25 then acc
    else aux_25 ((List.nth input_list i) :: acc) (i - 1)
  in
  aux_25 [] (index - 1)
(*  *)
let get_list_without i list =
  let rec aux acc cur_i list' =
    match (cur_i, list') with
    | (_, []) -> List.rev acc
    | (cur_i, _ :: tail) when cur_i = i -> aux acc (cur_i + 1) tail
    | (_, head :: tail) -> aux (head :: acc) (cur_i + 1) tail
  in
  aux [] 0 list
(*  *)
let sum_of_two number preamble_list = (* -> bool *)
  let check_index i = (* -> bool *)
    let list_without = get_list_without i preamble_list in
    let first_num = List.nth preamble_list i in
    let rec aux = function
      | [] -> false
      | n :: ns ->
        if first_num + n = number then true
        else aux ns
    in
    aux list_without
  in
  let rec check_all_indexes i = match i with
    | i when i < 0 -> false
    | i ->
      if check_index i then true
      else check_all_indexes (i - 1)
  in
  check_all_indexes 24
(*  *)
let valid_indexed_number index input_list = (* -> bool *)
  let preamble = get_previous_25 index input_list in
  let number = List.nth input_list index in
  sum_of_two number preamble
(*  *)
let get_first_invalid input =
  let length = List.length input in
  let rec aux i =
    if i = length then failwith "get_first_invalid - all are valid"
    else if valid_indexed_number i input then aux (i + 1)
    else (* i-th number is invalid *) List.nth input i
  in
  aux 25
(*  *)


let naloga1 content print_bool =
  let s = content
    |> String.trim
    |> String.split_on_char '\n'
    |> List.map int_of_string
    |> get_first_invalid
    |> string_of_int
  in
  if print_bool then
    let _ = print_endline ("day " ^ day ^ ", puzzle 1: " ^ s) in
    s
  else s
(*  *)


let list_slice_until m list = (* za skrajšanje inputa *)
  let rec aux acc i =
    let n = List.nth list i in
    if n = m then acc
    else aux (n :: acc) (i + 1)
  in
  List.rev (aux [] 0)
(*  *)
let n_sosedov_od_i_dalje n i list = (* -> seznam dolžine n *)
  let rec aux acc i' =
    if i' = i + n then List.rev acc
    else aux (List.nth list i' :: acc) (i' + 1)
  in
  aux [] i
(*  *)
let sum list = List.fold_left (+) 0 list (* list -> int *)
(*  *)
let poskusi_sosednjih_n n s1 input = (* Vrne seznam n-tih, če se seštejejo v s1 (option type) *)
  let length = List.length input in
  let rec poskusi_od_i_dalje i =
    if i = length - n + 1 then None (* indeksi pridejo že ven iz inputa *)
    else if sum (n_sosedov_od_i_dalje n i input) = s1 then Some (n_sosedov_od_i_dalje n i input)
    else poskusi_od_i_dalje (i + 1)
  in
  poskusi_od_i_dalje 0
(*  *)
let poskusi_vse s1 input = (* poskuša 2, 3, 4, ... dokler ne pride do ustrezne n-terice *)
  let rec aux_poskusi n =
    match poskusi_sosednjih_n n s1 input with
    | None -> aux_poskusi (n + 1)
    | Some sez -> sez
  in
  aux_poskusi 2
(*  *)
let min_plus_max_list list = (* za pridobitev končnega rezultata *)
  let mini list =
    let rec mini_aux cur_min = function
      | [] -> cur_min
      | x :: xs -> mini_aux (min x cur_min) xs
    in
    mini_aux (List.nth list 0) list
  in
  let maxi list =
    let rec maxi_aux cur_max = function
      | [] -> cur_max
      | x :: xs -> maxi_aux (max x cur_max) xs
    in
    maxi_aux (List.nth list 0) list
  in
  (mini list) + (maxi list)
(*  *)


let naloga2 content =
  let s1 = naloga1 content false |> int_of_string in
  let s2 = content
    |> String.trim
    |> String.split_on_char '\n'
    |> List.map int_of_string
    |> list_slice_until s1
    |> poskusi_vse s1
    |> min_plus_max_list
    |> string_of_int
  in
  print_endline ("day " ^ day ^ ", puzzle 2: " ^ s2);
  s2
(*  *)


let _ =
  let preberi_datoteko ime_datoteke =
    let chan = open_in ime_datoteke in
    let vsebina = really_input_string chan (in_channel_length chan) in
    close_in chan;
    vsebina
  in
  let izpisi_datoteko ime_datoteke vsebina =
    let chan = open_out ime_datoteke in
    output_string chan vsebina;
    close_out chan
  in

  let vsebina_datoteke = preberi_datoteko ("2020/data/day_" ^ day ^ ".in") in
  let odgovor1 = naloga1 vsebina_datoteke true in
  let odgovor2 = naloga2 vsebina_datoteke in

  izpisi_datoteko ("2020/out/day_" ^ day ^ "_1.out") odgovor1;
  izpisi_datoteko ("2020/out/day_" ^ day ^ "_2.out") odgovor2
(*  *)

(*
Danes kar lepa koda. Prva naloga super, pri drugi pa preverjamo
ogromno možnosti, ampak mislim da je to edini način.
Run time:  1. 58ms,  2. 250ms
*)