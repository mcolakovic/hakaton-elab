<?php

namespace App\Http\Controllers;

use App\Models\Vegetable;
use Illuminate\Http\Request;
use App\Http\Resources\VegetableR;

class VegetableController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        //
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        //
    }

    /**
     * Display the specified resource.
     */
    public function show(Vegetable $v)
    {
        return new Vegetable($v);
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(Vegetable $vegetable)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Vegetable $vegetable)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Vegetable $vegetable)
    {
        //
    }
}
