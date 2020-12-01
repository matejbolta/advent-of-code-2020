let day = "1"


let naloga1 vsebina_datoteke =
  let input_list = String.split_on_char '\n' (String.trim vsebina_datoteke) in
  let input_list = List.map int_of_string input_list in
  (* String.split_on_char : char -> string -> string list *)
  (* String.trim : string -> string *)

  let check_zeroth list =
    let rec aux_zeroth zeroth = function
      | [] -> None
      | x :: xs ->
        if x + zeroth = 2020 then Some (x, zeroth)
        else aux_zeroth zeroth xs
    in
    aux_zeroth (List.nth list 0) list
    (* List.nth : 'a list -> int -> 'a *)
  in

  let rec check_all = function
    | [] -> None
    | x :: xs ->
      match check_zeroth (x :: xs) with
      | Some (x, y) -> Some (x * y)
      | None -> check_all xs
  in
  
  let get_solution list =
    match (check_all list) with
    | None -> failwith "Oh dear Santa"
    | Some x -> x
  in

  let solution = string_of_int (get_solution input_list) in

  print_endline ("day " ^ day ^ ", puzzle 1: " ^ solution);
  solution
;;


let naloga2 vsebina_datoteke =
  let input_list = String.split_on_char '\n' (String.trim vsebina_datoteke) in
  let input_list = List.map int_of_string input_list in
  (* String.split_on_char : char -> string -> string list *)
  (* String.trim : string -> string *)

  let check_zeroth x list = (* Vrne zmnozek xyz, če obstajata y z, da x+y+z=2020 *)
    let rec aux_zeroth zeroth = function
      | [] -> None
      | y :: ys ->
        if x + zeroth + y = 2020 then Some (x, zeroth, y)
        else aux_zeroth zeroth ys
    in
    aux_zeroth (List.nth list 0) list
    (* List.nth : 'a list -> int -> 'a *)
  in

  let rec check_all_x x = function
    | [] -> None
    | y :: ys ->
      match check_zeroth x (y :: ys) with
      | Some (a, b, c) -> Some (a * b * c)
      | None -> check_all_x x ys
  in
  
  let rec check_all = function
    | [] -> None
    | x :: xs as l ->
      match check_all_x x l with
        | Some x -> Some (string_of_int x)
        | None -> check_all xs
  in

  let get_solution list =
    match (check_all list) with
    | None -> failwith "Oh dear Santa"
    | Some x -> x
  in

  let solution = get_solution input_list in

  print_endline ("day " ^ day ^ ", puzzle 2: " ^ solution);
  solution
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