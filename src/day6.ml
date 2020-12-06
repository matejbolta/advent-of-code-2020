# load "str.cma";;

let day = "6"

let count_group_1 list = (* 'a list -> int *)
  let rec aux seen_acc = function
  | [] -> List.length seen_acc
  | q :: qs when List.mem q seen_acc -> aux seen_acc qs
  | q :: qs -> aux (q :: seen_acc) qs
  in
  aux [] list
;;

let count_group_2 list = (* 'a list list -> int *)
  let rec count_aux acc = function (* Pelje se čez prvo osebo v grupi *)
  | [] -> acc
  | q :: qs ->
    if List.fold_left (&&) true (List.map (List.mem q) list)
    (* Če je q v vseh seznamih glavnega seznama *)
      then count_aux (acc + 1) qs
    else count_aux acc qs
  in
  count_aux 0 (List.nth list 0)
;;

let naloga1 vsebina_datoteke =
  let s = vsebina_datoteke
    |> String.trim
    |> Str.split (Str.regexp "\n\n")
    |> List.map (String.split_on_char '\n')
    |> List.map (String.concat "")
    |> List.map (Str.split (Str.regexp ""))
    |> List.map count_group_1
    |> List.fold_left (+) 0
    |> string_of_int
  in
  print_endline ("day " ^ day ^ ", puzzle 1: " ^ s);
  s
;;

let naloga2 vsebina_datoteke =
  let s = vsebina_datoteke
    |> String.trim
    |> Str.split (Str.regexp "\n\n")
    |> List.map (String.split_on_char '\n')
    |> List.map (List.map (Str.split (Str.regexp "")))
    (* At this point we have "c" list list list *)
    |> List.map count_group_2
    |> List.fold_left (+) 0
    |> string_of_int
  in
  print_endline ("day " ^ day ^ ", puzzle 2: " ^ s);
  s
;;

(* The nicest, most 'functional' solution so far. Ocaml is beautiful *)

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